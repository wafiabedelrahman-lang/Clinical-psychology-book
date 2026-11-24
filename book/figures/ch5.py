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

# 5-3 4Ps -------------------------------------------------------------------------
f = Fig(860, 330)
cells = [(440, 20, "1. العوامل المهيِّئة (Predisposing)", "ما الذي جعله أكثر قابلية؟\nاستعداد وراثي · صدمات مبكرة\nتفكك أسري · سمات شخصية", "slate"),
         (20, 20, "2. العوامل المفجِّرة (Precipitating)", "لماذا الآن؟\nوفاة · طلاق · نزوح\nفقد عمل", "amber"),
         (440, 170, "3. العوامل المديمة (Perpetuating)", "ما الذي يُبقي المشكلة؟ (أهداف العلاج)\nعزلة · تجنب · ضعف الدعم\nأفكار سلبية مستمرة", "rose"),
         (20, 170, "4. عوامل الحماية (Protective)", "ما الذي يساعد على التعافي؟\nإيمان وروحانية · ترابط أسري\nمهارات شخصية · دعم مجتمعي", "green")]
for x, y, t, b, c in cells:
    f.card(x, y, 400, 140, t, b, color=c, tsize=14, bsize=12.5)
f.save("fig-5-3-4ps.svg")

# 5-4 flow --------------------------------------------------------------------------
f = Fig(860, 150)
st = [("المقابلة", "الفصل 3", "teal"), ("إدارة الحالة", "الفصل 4", "slate"), ("التقييم", "المقاييس", "blue"),
      ("التشخيص", "DSM / ICD", "violet"), ("الصياغة", "4Ps", "amber"), ("خطة العلاج", "", "green")]
w = 120
x = 860 - 12 - w
for i, (t, b, c) in enumerate(st):
    f.rect(x, 40, w, 70, c, solid=(i == 5))
    col = "#fff" if i == 5 else C[c][0]
    f.text(x + w / 2, 66 if b else 75, t, size=14, weight=700, color=col)
    if b:
        f.text(x + w / 2, 92, b, size=11.5, color=MUTED)
    if i < 5:
        f.line(x - 2, 75, x - 18, 75, color=MUTED, arrow=True)
    x -= w + 20
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
