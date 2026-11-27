import math
from figlib import Fig, C, MUTED

# 5-1 DSM timeline ------------------------------------------------------------
f = Fig(860, 300)
eds = [("DSM-I", "1952", 106, "slate"), ("DSM-II", "1968", 182, "slate"), ("DSM-III", "1980", 265, "blue"),
       ("DSM-III-R", "1987", 292, "blue"), ("DSM-IV", "1994", 297, "teal"), ("IV-TR", "2000", 297, "teal"),
       ("DSM-5", "2013", 347, "violet"), ("DSM-5-TR", "2022", None, "violet")]
base = 240
step = 100
for i, (name, yr, n, c) in enumerate(eds):
    x = 800 - i * step
    if n:
        h = n * 0.5
        f.rect(x - 32, base - h, 64, h, c, r=4, solid=True)
        f.text(x, base - h - 14, str(n), size=13, weight=700, color=C[c][0])
    else:
        f.rect(x - 32, base - 20, 64, 20, c, r=4, dash="4 3")
        f.text(x, base - 34, "تحديث النص", size=11, color=C[c][0])
    f.text(x, base + 20, name, size=12, weight=700)
    f.text(x, base + 40, yr, size=11.5, color=MUTED)
f.line(40, base, 840, base, color=MUTED, sw=1.5)
f.text(430, 22, "عدد الفئات التشخيصية في كل طبعة", size=14, weight=700, color=C["blue"][0])
f.save("fig-5-1-dsm-timeline.svg")

# 5-2 axes to non-axial ----------------------------------------------------------
f = Fig(860, 330)
axes = ["المحور I: الاضطرابات الإكلينيكية", "المحور II: الشخصية والإعاقة العقلية", "المحور III: الحالات الطبية العامة",
        "المحور IV: الضغوط النفسية والاجتماعية", "المحور V: تقدير الأداء العام (GAF)"]
f.text(690, 26, "DSM-IV: خمسة محاور", size=15, weight=700, color=C["slate"][0])
for i, a in enumerate(axes):
    f.rect(540, 48 + i * 52, 300, 42, "slate")
    f.text(690, 69 + i * 52, a, size=12.5)
f.text(180, 26, "DSM-5: نظام غير محوري", size=15, weight=700, color=C["violet"][0])
f.rect(20, 48, 320, 146, "violet")
f.text(180, 121, "تشخيصات نفسية وطبية\n(المحاور I–III مدموجة)", size=13.5, weight=700, color=C["violet"][0])
f.rect(20, 204, 320, 42, "violet")
f.text(180, 225, "عوامل نفسية واجتماعية (رموز Z)", size=12.5)
f.rect(20, 256, 320, 42, "violet")
f.text(180, 277, "تقييم الإعاقة بمقياس WHODAS", size=12.5)
for y1, y2 in [(69, 121), (121, 121), (173, 121), (225, 225), (277, 277)]:
    f.path(f"M536,{y1} C440,{y1} 440,{y2} 344,{y2}", color=MUTED, arrow=True)
f.save("fig-5-2-axes.svg")

# 5-3 5Ps ---------------------------------------------------------------------------
f = Fig(860, 360)
cells = [(470, 15, "1. العوامل المهيِّئة (Predisposing)", "ما الذي زاد القابلية سابقًا؟\nاستعداد وراثي · صدمات مبكرة · تفكك أسري", "slate"),
         (20, 15, "2. العوامل المفجِّرة (Precipitating)", "لماذا الآن؟\nوفاة · طلاق · نزوح · فقد عمل", "amber"),
         (470, 215, "3. العوامل المديمة (Perpetuating)", "ما الذي يُبقي المشكلة؟ (أهداف العلاج)\nعزلة · تجنب · ضعف الدعم · أفكار سلبية", "rose"),
         (20, 215, "4. عوامل الحماية (Protective)", "ما نقاط القوة والموارد؟\nإيمان · ترابط أسري · مهارات · دعم مجتمعي", "green")]
for x, y, t, b, c in cells:
    f.card(x, y, 370, 130, t, b, color=c, tsize=13.5, bsize=12)
f.add(f'<ellipse cx="430" cy="180" rx="118" ry="58" fill="{C["blue"][0]}" stroke="#fff" stroke-width="4"/>')
f.text(430, 165, "المشكلة الحالية", size=15, color="#fff", weight=700)
f.text(430, 192, "(Presenting) الأعراض\nوالمخاطر والاحتياجات", size=11.5, color="#fff")
f.text(430, 350, "الشخص في سياقه — والصياغة فرضية قابلة للمراجعة", size=12, color=MUTED)
f.save("fig-5-3-4ps.svg")

# 5-4 circular pathway ----------------------------------------------------------------
f = Fig(860, 360)
steps = [("المقابلة", "teal"), ("التقييم", "blue"), ("فرضيات تشخيصية", "slate"), ("تشخيص تفريقي", "slate"),
         ("التشخيص", "violet"), ("الصياغة", "amber"), ("خطة التدخل", "green"), ("الإحالة", "rose"), ("المتابعة", "teal")]
n = len(steps)
cx, cy, rx, ry = 430, 175, 330, 130
pts = []
for i in range(n):
    th = math.pi / 2 + i * 2 * math.pi / n
    pts.append((cx + rx * math.cos(th), cy - ry * math.sin(th)))
for i in range(n):
    x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % n]
    col = C["amber"][0] if i == n - 1 else MUTED
    f.path(f"M{x1 + (x2 - x1) * 0.3:.0f},{y1 + (y2 - y1) * 0.3:.0f} L{x1 + (x2 - x1) * 0.7:.0f},{y1 + (y2 - y1) * 0.7:.0f}", color=col, sw=2, arrow=True)
for (x, y), (t, c) in zip(pts, steps):
    f.rect(x - 70, y - 22, 140, 44, c, solid=(t in ("التشخيص", "الصياغة")))
    f.text(x, y, t, size=13, weight=700, color="#fff" if t in ("التشخيص", "الصياغة") else C[c][0])
f.text(cx, cy - 8, "المسار دائري", size=15, weight=700, color=C["blue"][0])
f.text(cx, cy + 18, "نتائج المتابعة تعيدنا\nإلى التقييم والصياغة", size=12, color=MUTED)
f.save("fig-5-4-flow.svg")

# 5-5 funnel -------------------------------------------------------------------------
f = Fig(860, 320)
layers = [("كل من يراجع المؤسسة: يُطبَّق عليه مقياس فرز قصير", 760, "teal"),
          ("من تجاوز نقطة القطع: «فرز إيجابي»", 560, "blue"),
          ("مقابلة إكلينيكية", 380, "violet"),
          ("التشخيص أو نفيه", 220, "amber")]
y = 20
for t, w, c in layers:
    x = 430 - w / 2
    f.add(f'<path d="M{x},{y} h{w} l-40,62 h{-(w - 80)} z" fill="{C[c][0]}" opacity="0.92"/>')
    f.text(430, y + 31, t, size=13.5, color="#fff", weight=700)
    y += 68
f.text(430, 306, "المقياس يختصر الطريق إلى من يحتاج التقييم، ولا يغني عن المقابلة", size=12, color=MUTED)
f.save("fig-5-5-funnel.svg")

# 5-6 C-SSRS ladder -------------------------------------------------------------------
f = Fig(860, 340)
rungs = [("1. تمني الموت", "يُسأل دائمًا", "green"), ("2. أفكار فعلية لقتل النفس", "يُسأل دائمًا", "teal"),
         ("3. التفكير في طريقة", "إن كانت (2) نعم", "amber"), ("4. نية", "إن كانت (2) نعم", "amber"),
         ("5. خطة", "إن كانت (2) نعم", "rose"), ("6. سلوك انتحاري (مدى الحياة / 3 أشهر)", "يُسأل دائمًا", "rose")]
for i, (t, b, c) in enumerate(rungs):
    y = 262 - i * 48
    x = 470 - i * 40
    f.rect(x, y, 360, 40, c, solid=(i >= 3))
    col = "#fff" if i >= 3 else C[c][0]
    f.text(x + 230, y + 20, t, size=13, weight=700, color=col)
    f.text(x + 60, y + 20, b, size=11, color="#fff" if i >= 3 else MUTED)
f.path("M250,280 L100,30", color=C["rose"][0], sw=3, arrow=True)
f.text(105, 170, "يرتفع\nالخطر", size=14, weight=700, color=C["rose"][0])
f.text(430, 326, "الإجابة بنعم عن النية أو الخطة أو سلوك حديث = خطر مرتفع يستلزم تدخلًا فوريًا", size=12, color=MUTED)
f.save("fig-5-6-cssrs.svg")

# 5-7 follow-up curve ------------------------------------------------------------------
f = Fig(860, 300)
x0, x1, y0, y1 = 120, 760, 250, 40
def px(i):
    return x1 - i * (x1 - x0) / 2
def py(v):
    return y0 - v / 60 * (y0 - y1)
f.add(f'<rect x="{x0}" y="{py(33)}" width="{x1 - x0}" height="{py(31) - py(33)}" fill="{C["amber"][1]}" stroke="{C["amber"][0]}" stroke-dasharray="4 3"/>')
f.text(x1 - 4, py(33) - 14, "نطاق نقطة القطع 31–33", size=11.5, color=C["amber"][0], anchor="start")
for v in (0, 20, 40, 60):
    f.line(x0, py(v), x1, py(v), color="#e3e9ee", sw=1)
    f.text(x1 + 22, py(v), str(v), size=11, color=MUTED)
pts = [(0, 46), (1, 38), (2, 24)]
d = "M" + " L".join(f"{px(i):.0f},{py(v):.0f}" for i, v in pts)
f.path(d, color=C["blue"][0], sw=3)
for i, v in pts:
    f.circle(px(i), py(v), 7, "blue", solid=True)
    f.text(px(i), py(v) - 20, str(v), size=14, weight=700, color=C["blue"][0])
    f.text(px(i), y0 + 24, ["الجلسة 1", "الجلسة 4", "الجلسة 8"][i], size=12.5)
f.save("fig-5-7-curve.svg")

# 5-8 measure across stages --------------------------------------------------------------
f = Fig(860, 170)
st = [("الاستقبال", "مقياس فرز", "teal"), ("التشخيص والصياغة", "المقابلة + بنود الخطر", "blue"),
      ("التدخل", "خط الأساس", "violet"), ("المتابعة", "إعادة القياس", "amber"), ("الإغلاق", "تقييم نهائي", "green")]
w = 150
x = 860 - 15 - w
for i, (t, b, c) in enumerate(st):
    f.card(x, 30, w, 100, t, b, color=c, tsize=13.5, bsize=12)
    if i < 4:
        f.line(x - 2, 80, x - 18, 80, color=MUTED, arrow=True)
    x -= w + 22
f.text(430, 155, "يدخل المقياس في كل مرحلة، من الاستقبال حتى إغلاق الملف", size=12, color=MUTED)
f.save("fig-5-8-stages.svg")
print("ch5 figures done")
