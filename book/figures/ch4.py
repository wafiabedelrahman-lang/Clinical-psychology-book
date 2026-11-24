import math
from figlib import Fig, C, MUTED

# 4-1 six-step cycle ----------------------------------------------------------
f = Fig(860, 380)
steps = [("1. الاستقبال", "القبول · الإدخال", "slate"), ("2. التقييم", "التقييم الشامل", "teal"),
         ("3. التخطيط", "خطة الرعاية", "blue"), ("4. الإحالة", "التنفيذ · التنسيق", "violet"),
         ("5. المتابعة", "المراقبة", "amber"), ("6. الإغلاق", "التخريج", "green")]
cx, cy, rx, ry = 430, 190, 300, 135
pos = []
for i in range(6):
    th = math.pi / 2 + i * math.pi / 3
    pos.append((cx + rx * math.cos(th), cy - ry * math.sin(th)))
for i in range(6):
    x1, y1 = pos[i]
    x2, y2 = pos[(i + 1) % 6]
    if i < 5:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        f.path(f"M{x1 + (x2 - x1) * 0.38:.0f},{y1 + (y2 - y1) * 0.38:.0f} L{x1 + (x2 - x1) * 0.62:.0f},{y1 + (y2 - y1) * 0.62:.0f}", color=MUTED, arrow=True)
# dashed return arrow from follow-up to assessment
x5, y5 = pos[4]
x2_, y2_ = pos[1]
f.path(f"M{x5 - 40:.0f},{y5 - 38:.0f} Q{cx:.0f},{cy + 40:.0f} {x2_ + 60:.0f},{y2_ + 38:.0f}", color=C["amber"][0], arrow=True)
for (x, y), (t, b, c) in zip(pos, steps):
    f.card(x - 92, y - 36, 184, 72, t, b, color=c, tsize=14, bsize=11.5)
f.text(cx + 60, cy - 30, "قد تعيدنا المتابعة\nإلى التقييم أو التخطيط", size=11.5, color=C["amber"][0])
f.save("fig-4-1-steps.svg")

# 4-2 biopsychosocial -------------------------------------------------------------
f = Fig(860, 340)
circles = [(360, 130, "بيولوجي", "أمراض مزمنة · أدوية\nحمل وولادة · نمو", "rose", 560, 70),
           (500, 130, "نفسي", "أعراض · حالة عقلية\nمخاطر · قوة نفسية", "violet", 300, 70),
           (430, 235, "اجتماعي", "أسرة · سكن · دخل\nتعليم · قانون", "teal", 430, 320)]
for x, y, t, b, c, lx, ly in circles:
    dark, light = C[c]
    f.add(f'<circle cx="{x}" cy="{y}" r="105" fill="{dark}" fill-opacity="0.13" stroke="{dark}" stroke-width="2"/>')
for x, y, t, b, c, lx, ly in circles:
    dx = (x - 430) * 1.0
    dy = (y - 165) * 1.0
    f.text(x + dx * 0.95, y + dy * 0.75 - 12, t, size=16, weight=700, color=C[c][0])
    f.text(x + dx * 0.95, y + dy * 0.75 + 16, b, size=11.5)
f.circle(430, 168, 34, "amber", solid=True)
f.text(430, 168, "المستفيد", size=13, color="#fff", weight=700)
f.text(140, 300, "Engel (1977)", size=11.5, color=MUTED)
f.save("fig-4-2-biopsychosocial.svg")

# 4-3 genogram -----------------------------------------------------------------------
f = Fig(860, 360)
def male(x, y, label, dead=False):
    f.add(f'<rect x="{x - 22}" y="{y - 22}" width="44" height="44" fill="#fff" stroke="#1d2a3a" stroke-width="2"/>')
    if dead:
        f.line(x - 22, y - 22, x + 22, y + 22, color="#1d2a3a", sw=2)
        f.line(x + 22, y - 22, x - 22, y + 22, color="#1d2a3a", sw=2)
    f.text(x, y + 40, label, size=12)
def female(x, y, label, dead=False, client=False):
    f.add(f'<circle cx="{x}" cy="{y}" r="22" fill="#fff" stroke="#1d2a3a" stroke-width="2"/>')
    if client:
        f.add(f'<circle cx="{x}" cy="{y}" r="15" fill="none" stroke="#1d2a3a" stroke-width="2"/>')
    if dead:
        f.line(x - 16, y - 16, x + 16, y + 16, color="#1d2a3a", sw=2)
        f.line(x + 16, y - 16, x - 16, y + 16, color="#1d2a3a", sw=2)
    f.text(x, y + 40, label, size=12)
# grandparents (mother's side)
male(560, 50, "الجد (متوفى)", dead=True); female(680, 50, "الجدة")
f.line(582, 50, 658, 50, color="#1d2a3a", sw=2)
f.line(620, 50, 620, 110, color="#1d2a3a", sw=2)
# parents
male(320, 140, "الأب"); female(620, 140, "الأم")
f.line(342, 140, 598, 140, color="#1d2a3a", sw=2)
f.line(470, 140, 470, 215, color="#1d2a3a", sw=2)
f.line(300, 215, 640, 215, color="#1d2a3a", sw=2)
for x in (300, 470, 640):
    f.line(x, 215, x, 245, color="#1d2a3a", sw=2)
male(640, 267, "أخ (شهيد)", dead=True)
female(470, 267, "المستفيدة", client=True)
female(300, 267, "الأخت الكبرى")
# relationship lines
f.path("M490,250 Q560,190 600,160", color=C["green"][0], sw=4)
f.path("M450,275 q-25,-12 -50,0 q-25,12 -50,0 q-15,-7 -28,-4", color=C["rose"][0], sw=2.5)
f.rect(40, 70, 190, 120, "slate", r=8)
f.add(f'<line x1="60" y1="100" x2="110" y2="100" stroke="{C["green"][0]}" stroke-width="4"/>')
f.text(200, 100, "علاقة قوية", size=12, anchor="start")
f.add(f'<path d="M60,135 q12,-8 25,0 q12,8 25,0" stroke="{C["rose"][0]}" stroke-width="2.5" fill="none"/>')
f.text(200, 135, "علاقة متوترة", size=12, anchor="start")
f.text(200, 168, "□ ذكر  ○ أنثى  X متوفى", size=11.5, anchor="start")
f.save("fig-4-3-genogram.svg")

# 4-4 countdown -------------------------------------------------------------------------
f = Fig(860, 170)
items = [("«بقيت ثلاث جلسات»", "teal"), ("«بقيت جلستان»", "blue"), ("«الأسبوع القادم آخر لقاء»", "violet"), ("جلسة الإغلاق", "green")]
w = 185
x = 860 - 20 - w
for i, (t, c) in enumerate(items):
    f.rect(x, 45, w, 64, c, solid=(i == 3))
    f.text(x + w / 2, 77, t, size=13.5, weight=700, color="#fff" if i == 3 else C[c][0])
    if i < 3:
        f.line(x - 3, 77, x - 22, 77, color=MUTED, arrow=True)
    x -= w + 25
f.text(430, 145, "الإنهاء المفاجئ قد يُشعر المستفيد بالتخلي؛ والعد التنازلي يمنحه فرصة لقول ما لم يقله بعد", size=12, color=MUTED)
f.save("fig-4-4-countdown.svg")

# 4-5 pre/post ----------------------------------------------------------------------------
f = Fig(860, 280)
base = 235
scale = 6
f.line(200, base, 660, base, color=MUTED, sw=1.5)
for x, v, lab, c in [(540, 30, "القياس القبلي", "rose"), (320, 14, "القياس البعدي", "teal")]:
    h = v * scale
    f.rect(x - 60, base - h, 120, h, c, r=4, solid=True)
    f.text(x, base - h - 16, str(v), size=18, weight=700, color=C[c][0])
    f.text(x, base + 22, lab, size=13)
f.path("M470,60 Q430,40 390,140", color=MUTED, arrow=True)
f.text(760, 120, "انخفاض نحو 53%\n(30 − 14) ÷ 30", size=14, weight=700, color=C["blue"][0])
f.save("fig-4-5-prepost.svg")

# 4-6 coding -------------------------------------------------------------------------------
f = Fig(860, 240)
f.card(520, 30, 300, 170, "ملف الحالة: SH-1", "ملاحظات · تقييم · خطة · متابعة\n\nلا يظهر فيه الاسم الصريح", color="blue", tsize=15, bsize=12.5)
f.card(40, 30, 300, 170, "مفتاح الرموز", "SH-1 ← المستفيدة (أ)\nSH-2 ← المستفيدة (ب)\n\nملف محمي ومنفصل\nلصاحب الصلاحية فقط", color="rose", tsize=15, bsize=12.5)
f.line(510, 115, 350, 115, color=MUTED, sw=2, dash="6 6")
f.text(430, 98, "لا يجتمعان", size=13, weight=700, color=C["rose"][0])
f.text(430, 225, "الرمز = الحرفان الأولان من اسم مدير الحالة + رقم الحالة (مثال المحاضِرة)", size=11.5, color=MUTED)
f.save("fig-4-6-coding.svg")
print("ch4 figures done")
