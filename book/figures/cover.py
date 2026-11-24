"""Cover artwork: five linked circles (understand, assess, intervene, prevent, research)."""
import math
W, H = 640, 330
cx, cy, R = 320, 165, 120
words = ["فهم", "تقييم", "تدخل", "وقاية", "بحث"]
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
pts = []
for i, w in enumerate(words):
    a = -math.pi / 2 + i * 2 * math.pi / 5
    pts.append((cx + R * math.cos(a), cy + R * math.sin(a), w))
for i in range(5):
    for j in range(i + 1, 5):
        x1, y1, _ = pts[i]; x2, y2, _ = pts[j]
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#ffffff" stroke-opacity="0.18" stroke-width="1.2"/>')
parts.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#f0c27b" stroke-opacity="0.55" stroke-width="1.5" stroke-dasharray="4 6"/>')
parts.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="#ffffff" fill-opacity="0.12" stroke="#ffffff" stroke-opacity="0.6"/>')
parts.append(f'<text x="{cx}" y="{cy}" fill="#ffffff" font-size="17" font-weight="700" text-anchor="middle" dominant-baseline="middle" font-family="Noto Kufi Arabic">الإنسان</text>')
for x, y, w in pts:
    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="34" fill="#ffffff" fill-opacity="0.95"/>')
    parts.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="#1f5f7a" font-size="15" font-weight="700" text-anchor="middle" dominant-baseline="middle" font-family="Noto Kufi Arabic">{w}</text>')
parts.append("</svg>")
open("cover-art.svg", "w", encoding="utf-8").write("".join(parts))
