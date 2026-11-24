"""Small helper library for drawing the book's figures as SVG with one shared style.

Every figure is RTL Arabic text on a white card. Colours are defined once here so all
figures in the book match.
"""
from xml.sax.saxutils import escape

INK = "#1d2a3a"
MUTED = "#5b6b78"
LINE = "#9fb3c2"
C = {
    "blue": ("#1f5f7a", "#e6f0f5"),
    "teal": ("#2b7f78", "#e5f3f1"),
    "amber": ("#b7792a", "#fbf1e2"),
    "rose": ("#a2475e", "#f8e9ee"),
    "violet": ("#5b4f99", "#eeecf8"),
    "slate": ("#4a5a68", "#eef1f4"),
    "green": ("#3f7d3a", "#e9f4e7"),
}
FONT = "'Noto Kufi Arabic', 'Noto Naskh Arabic', sans-serif"


class Fig:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    # --- primitives -------------------------------------------------------
    def rect(self, x, y, w, h, color="blue", r=10, solid=False, stroke=True, sw=1.5, dash=None):
        dark, light = C[color]
        fill = dark if solid else light
        st = f'stroke="{dark}" stroke-width="{sw}"' if stroke else 'stroke="none"'
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" {st}{da}/>')

    def circle(self, cx, cy, r, color="blue", solid=False, sw=1.5):
        dark, light = C[color]
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{dark if solid else light}" stroke="{dark}" stroke-width="{sw}"/>')

    def text(self, x, y, s, size=15, color=INK, weight=400, anchor="middle", lines_gap=None):
        """Draw text; `s` may contain '\n' for several centred lines."""
        lines = s.split("\n")
        gap = lines_gap or size * 1.45
        y0 = y - (len(lines) - 1) * gap / 2
        for i, ln in enumerate(lines):
            self.add(
                f'<text x="{x}" y="{y0 + i * gap:.1f}" font-size="{size}" fill="{color}" '
                f'font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="middle" '
                f'direction="rtl" font-family="{FONT}">{escape(ln)}</text>'
            )

    def line(self, x1, y1, x2, y2, color=LINE, sw=2, arrow=False, dash=None):
        m = ' marker-end="url(#arr)"' if arrow else ""
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{m}{da}/>')

    def path(self, d, color=LINE, sw=2, arrow=False, fill="none"):
        m = ' marker-end="url(#arr)"' if arrow else ""
        self.add(f'<path d="{d}" stroke="{color}" stroke-width="{sw}" fill="{fill}"{m}/>')

    # --- composite helpers --------------------------------------------------
    def card(self, x, y, w, h, title, body=None, color="blue", tsize=16, bsize=13):
        """A box with a solid header strip and optional body text."""
        dark, light = C[color]
        self.rect(x, y, w, h, color)
        if body is None:
            self.text(x + w / 2, y + h / 2, title, size=tsize, color=dark, weight=700)
            return
        hh = tsize * 2.3
        self.add(f'<path d="M{x},{y + hh} v{-(hh - 10)} a10,10 0 0 1 10,-10 h{w - 20} a10,10 0 0 1 10,10 v{hh - 10} z" fill="{dark}"/>')
        self.text(x + w / 2, y + hh / 2 + 1, title, size=tsize, color="#ffffff", weight=700)
        self.text(x + w / 2, y + hh + (h - hh) / 2, body, size=bsize, color=INK)

    def pill(self, x, y, w, h, s, color="blue", size=14, solid=True):
        self.rect(x, y, w, h, color, r=h / 2, solid=solid)
        self.text(x + w / 2, y + h / 2, s, size=size, color="#ffffff" if solid else C[color][0], weight=700)

    def save(self, path):
        defs = (
            '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker></defs>'
        )
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" role="img">{defs}'
            f'<rect width="{self.w}" height="{self.h}" fill="#ffffff"/>' + "".join(self.parts) + "</svg>"
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
