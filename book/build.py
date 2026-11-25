#!/usr/bin/env python3
"""Build the clinical psychology course book: Markdown chapters -> one HTML -> PDF.

Usage:  python3 book/build.py            (from the repository root)
Output: book/build/book.html and the PDF named in OUT_PDF.
"""
import re
import subprocess
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent
ROOT = BOOK.parent
BUILD = BOOK / "build"
OUT_PDF = ROOT / "كتاب_علم_النفس_الإكلينيكي_د_عبد_الرحمن_وافي.pdf"

AUTHOR = "د. عبد الرحمن جمعة وافي"
ROLE = ["محاضر متعاون بقسم علم النفس – جامعة الأقصى", "دكتوراه علم النفس الإكلينيكي"]
TITLE = "علم النفس الإكلينيكي"
SUBTITLE = "المقابلة والتقييم والتشخيص وإدارة الحالة في الممارسة الميدانية"
YEAR = "2026"

FRONT = ["00-preface.md"]
CHAPTERS = [
    "01-introduction.md",
    "02-psychologist-team.md",
    "03-interview.md",
    "04-case-management.md",
    "05-diagnosis-assessment.md",
    "06-suicide-risk.md",
]
BACK = ["89-appendix.md", "90-glossary.md", "91-references.md"]

# (lecture number, title, chapter number, source note)
LECTURES = [
    (1, "مدخل إلى علم النفس الإكلينيكي", 1, ""),
    (2, "تاريخ علم النفس الإكلينيكي وتطوره", 1, "مسجلة مرئيًا، وكُتب نصها من المادة التاريخية في المحاضرات"),
    (3, "من هو الأخصائي النفسي الإكلينيكي؟ أدواره المهنية", 2, ""),
    (4, "أخلاقيات الأخصائي النفسي وسماته وإعداده", 2, ""),
    (5, "الفريق العلاجي متعدد التخصصات والتطبيق الميداني", 2, ""),
    (6, "المقابلة الإكلينيكية (1): مفهومها وأنواعها ومراحلها", 3, ""),
    (7, "المقابلة الإكلينيكية (2): مهارات كل مرحلة", 3, ""),
    (8, "المقابلة الإكلينيكية (3): ما وراء الكلمات وتقييم المقابلة", 3, ""),
    (9, "إدارة الحالة (1): المفهوم والمبادئ والتقييم الشامل", 4, "قدّمتها أ. شيماء حمدان"),
    (10, "إدارة الحالة (2): من خطة الرعاية إلى الإغلاق والتوثيق", 4, "قدّمتها أ. شيماء حمدان"),
    (11, "التشخيص النفسي والصياغة الإكلينيكية", 5, ""),
    (12, "الاختبارات والمقاييس النفسية", 5, ""),
    (13, "تقييم خطر الانتحار", 6, ""),
]
CH_NAMES = {}


def sh(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        sys.exit(f"command failed: {' '.join(map(str, cmd))}\n{r.stderr}")
    return r.stdout


def md_to_html(path: Path) -> str:
    return sh(["pandoc", str(path), "-f", "markdown+fenced_divs+pipe_tables+header_attributes",
               "-t", "html5", "--wrap=none"])


def inline_figures(html: str) -> str:
    """Replace <img src="figures/x.svg"> by the SVG itself (web fonts do not reach <img> SVGs)
    and prefix captions with the figure number taken from the id (fig:1-2 -> الشكل 1-2)."""

    def svg_for(src):
        svg = (BOOK / src).read_text(encoding="utf-8")
        return re.sub(r'width="\d+" height="\d+"', "", svg, count=1)

    def fig(m):
        block = m.group(0)
        fid = re.search(r'id="fig:([\d-]+)"', block)
        src = re.search(r'src="([^"]+\.svg)"', block)
        cap = re.search(r"<figcaption>(.*?)</figcaption>", block, re.S)
        num = fid.group(1) if fid else ""
        caption = cap.group(1) if cap else ""
        label = f'<span class="fignum">الشكل {num}:</span> ' if num else ""
        return f'<figure id="fig-{num}">{svg_for(src.group(1))}<figcaption>{label}{caption}</figcaption></figure>'

    html = re.sub(r"<figure[^>]*>.*?</figure>", fig, html, flags=re.S)
    return html


def collect_toc(html: str):
    items = []
    for m in re.finditer(r'<h([12])([^>]*)>(.*?)</h\1>', html, re.S):
        level, attrs, text = m.groups()
        hid = re.search(r'id="([^"]+)"', attrs)
        cls = re.search(r'class="([^"]+)"', attrs)
        if not hid or not cls:
            continue
        hid, cls = hid.group(1), cls.group(1)
        text = re.sub(r"<[^>]+>", "", text).strip()
        if "chapter" in cls:
            items.append(("ch", hid, text))
        elif "lecture" in cls:
            items.append(("lec", hid, text))
        elif "backmatter" in cls:
            items.append(("back", hid, text))
    return items


def cover_html():
    art = (BOOK / "figures" / "cover-art.svg").read_text(encoding="utf-8")
    role = "<br>".join(ROLE)
    return f"""
<section class="cover"><div class="band"></div><div class="inner">
  <div class="kicker">مقرر مساق علم النفس الإكلينيكي — برنامج بكالوريوس علم النفس والإرشاد النفسي</div>
  <h1 class="title">{TITLE}</h1>
  <div class="subtitle">{SUBTITLE}</div>
  <div class="rule"></div>
  <div class="art">{art}</div>
  <div class="author"><div class="name">{AUTHOR}</div><div class="role">{role}</div>
  <div class="edition">الطبعة الأولى — {YEAR}</div></div>
</div></section>
<section class="titlepage">
  <h1>{TITLE}</h1>
  <div class="sub">{SUBTITLE}</div>
  <div class="by">تأليف<br>{AUTHOR}</div>
  <div class="role">{"<br>".join(ROLE)}</div>
  <div class="meta">كتاب المساق: يجمع محاضرات المساق الثلاث عشرة في ستة فصول<br>الطبعة الأولى {YEAR}</div>
</section>"""


def toc_html(items, pages=None):
    pages = pages or {}

    def entry(cls, hid, text):
        pg = pages.get(hid, "")
        return (f'<li class="{cls}"><a href="#{hid}"><span class="t">{text}</span>'
                f'<span class="dots"></span><span class="pg">{pg}</span></a></li>')

    out = ['<h1 class="fronthead" id="toc">فهرس المحتويات</h1><nav class="toc"><ul>']
    out.append(entry("toc-back", "preface", "مقدمة الكتاب"))
    out.append(entry("toc-back", "lecture-index", "فهرس المحاضرات"))
    for kind, hid, text in items:
        out.append(entry({"ch": "toc-ch", "lec": "toc-lec", "back": "toc-back"}[kind], hid, text))
    out.append("</ul></nav>")
    return "\n".join(out)


def add_markers(html, ids):
    """Pass 1 only: put an invisible ASCII marker inside each heading so its page can be found."""
    for hid in ids:
        html = re.sub(rf'(<h[12][^>]*id="{re.escape(hid)}"[^>]*>)', rf'\1<span class="mk">QQ{hid}QQ</span>', html, count=1)
    return html


def heading_pages(pdf_path):
    pages = {}
    n = int(re.search(r"Pages:\s+(\d+)", sh(["pdfinfo", str(pdf_path)])).group(1))
    for pg in range(1, n + 1):
        txt = sh(["pdftotext", "-f", str(pg), "-l", str(pg), str(pdf_path), "-"])
        for hid in re.findall(r"QQ([A-Za-z0-9_-]+)QQ", txt):
            pages.setdefault(hid, pg)
    return pages


def lecture_index_html(items):
    lec_ids = [hid for kind, hid, _ in items if kind == "lec"]
    ch_titles = {}
    n = 0
    for kind, hid, text in items:
        if kind == "ch":
            n += 1
            ch_titles[n] = text.split(":", 1)[-1].strip()
    rows = []
    for (num, title, ch, note) in LECTURES:
        hid = f"l{num}"
        link = f'<a href="#{hid}">{title}</a>' if hid in lec_ids else title
        note_html = f'<br><small>({note})</small>' if note else ""
        rows.append(f"<tr><td>{num}</td><td>{link}{note_html}</td>"
                    f'<td class="ch">الفصل {ch}</td><td>{ch_titles.get(ch, "")}</td></tr>')
    per_ch = {}
    for _, _, ch, _ in LECTURES:
        per_ch[ch] = per_ch.get(ch, 0) + 1
    counts = "، ".join(f"الفصل {c}: {k} {'محاضرة' if k == 1 else ('محاضرتان' if k == 2 else 'محاضرات')}"
                      for c, k in sorted(per_ch.items()))
    return f"""<h1 class="fronthead" id="lecture-index">فهرس المحاضرات</h1>
<p>يضم الكتاب <strong>{len(LECTURES)} محاضرة</strong> موزعة على <strong>{len(per_ch)} فصول</strong>. ويبين الجدول موضع كل محاضرة في الكتاب.</p>
<table class="lecture-index"><thead><tr><th>رقم</th><th>المحاضرة</th><th>الفصل</th><th>عنوان الفصل</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table>
<div class="note"><strong>عدد محاضرات كل فصل:</strong> {counts}.</div>"""


def page_rules(n_chapters, chapter_titles):
    rules = []
    for n in range(1, n_chapters + 1):
        t = chapter_titles.get(n, "").replace('"', "")
        rules.append(f'@page ch{n} {{ @top-center {{ content: "{t}"; }} }}')
    rules.append('@page back { @top-center { content: "ملاحق الكتاب"; } }')
    return "\n".join(rules)


def main():
    BUILD.mkdir(exist_ok=True)
    for script in sorted((BOOK / "figures").glob("ch*.py")) + [BOOK / "figures" / "cover.py"]:
        if script.exists():
            sh([sys.executable, script.name], cwd=BOOK / "figures")
    sections, titles = [], {}
    n = 0
    for name in CHAPTERS:
        p = BOOK / "chapters" / name
        if p.exists():
            n += 1
            h = inline_figures(md_to_html(p))
            m = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
            titles[n] = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""
            sections.append(f'<section class="chap" style="page: ch{n}">{h}</section>')
    for name in BACK:
        p = BOOK / "chapters" / name
        if p.exists():
            sections.append(f'<section class="chap" style="page: back">{inline_figures(md_to_html(p))}</section>')
    body_html = "\n".join(sections)
    items = collect_toc(body_html)
    front = "".join(md_to_html(BOOK / "chapters" / f) for f in FRONT if (BOOK / "chapters" / f).exists())
    out = BUILD / "book.html"

    def write(pages, markers=False):
        html = f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<title>{TITLE} — {AUTHOR}</title>
<link rel="stylesheet" href="../assets/style.css">
<style>{page_rules(n, titles)}</style>
</head><body>
{cover_html()}
<section class="front">{front}
{lecture_index_html(items)}
{toc_html(items, pages)}</section>
{body_html}
</body></html>"""
        if markers:
            html = add_markers(html, [h for h, _ in ids_titles])
        out.write_text(html, encoding="utf-8")

    # pass 1: placeholder page numbers (same width) -> find real pages -> pass 2
    ids_titles = [("preface", "مقدمة الكتاب"), ("lecture-index", "فهرس المحاضرات")] + [(h, t) for _, h, t in items]
    write({h: "000" for h, _ in ids_titles}, markers=True)
    sh(["node", str(BOOK / "render.js"), str(out), str(OUT_PDF)])
    pages = heading_pages(OUT_PDF)
    missing = [h for h, _ in ids_titles if h not in pages]
    if missing:
        print("warning: no page found for", missing)
    write(pages)
    sh(["node", str(BOOK / "render.js"), str(out), str(OUT_PDF)])
    print("pdf:", OUT_PDF)


if __name__ == "__main__":
    main()
