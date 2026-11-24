from figlib import Fig, C, MUTED

# 1-1 five words ------------------------------------------------------------
f = Fig(860, 250)
f.text(430, 30, "علم النفس الإكلينيكي في خمس كلمات", size=18, weight=700, color=C["blue"][0])
items = [
    ("فهم", "وصف السلوك\nومعرفة أسبابه", "blue"),
    ("تقييم", "جمع المعلومات\nوقياسها وتشخيصها", "teal"),
    ("تدخل", "العلاج ومساعدة\nالشخص على التغيير", "violet"),
    ("وقاية", "منع المشكلات\nقبل تفاقمها", "amber"),
    ("بحث", "اختبار الأدلة\nوتطوير المعرفة", "rose"),
]
w, gap = 150, 17
x = 860 - 18 - w
for i, (t, b, c) in enumerate(items):
    f.card(x, 62, w, 160, t, b, color=c, tsize=18, bsize=13)
    if i < 4:
        f.line(x - 2, 142, x - gap + 3, 142, color=MUTED, sw=1.5, arrow=True)
    x -= w + gap
f.save("fig-1-1-five-words.svg")

# 1-2 criteria ----------------------------------------------------------------
f = Fig(860, 300)
f.circle(430, 160, 70, "blue", solid=True)
f.text(430, 160, "هل يحتاج السلوك\nإلى مساعدة؟", size=15, color="#fff", weight=700)
crit = [
    (650, 85, "الشدة والمعاناة", "ما مقدار الألم الذي\nيشعر به الشخص؟", "rose"),
    (210, 85, "تأثر الأداء", "هل يعطّل الدراسة أو\nالعمل أو العلاقات؟", "amber"),
    (650, 235, "البعد عن المألوف", "هل هو نادر مقارنة بما\nيفعله أغلب الناس؟", "teal"),
    (210, 235, "السياق والثقافة", "هل هو متوقع في هذا\nالموقف وهذه الثقافة؟", "violet"),
]
for cx, cy, t, b, c in crit:
    f.card(cx - 105, cy - 55, 210, 110, t, b, color=c, tsize=15, bsize=12.5)
    f.line(430 + (cx - 430) * 0.33, 160 + (cy - 160) * 0.55, cx - 105 if cx > 430 else cx + 105, cy, color=C[c][0], sw=1.5)
f.text(430, 285, "لا نحكم بمعيار واحد، ولا من موقف واحد، ولا بمعزل عن الظروف", size=13, color=MUTED)
f.save("fig-1-2-criteria.svg")

# 1-3 scientist practitioner cycle -------------------------------------------
f = Fig(860, 300)
nodes = [(430, 60, "الميدان", "حالات حقيقية وأسئلة\nتنبع من الواقع", "teal"),
         (680, 220, "البحث", "أدلة ومقاييس ونظريات\nتُختبر", "blue"),
         (180, 220, "الممارسة", "قرارات وتدخلات\nمبنية على ما ثبت", "amber")]
for cx, cy, t, b, c in nodes:
    f.card(cx - 110, cy - 48, 220, 96, t, b, color=c, tsize=16, bsize=12.5)
f.path("M545,80 Q650,90 690,168", color=MUTED, arrow=True)
f.path("M568,232 L295,232", color=MUTED, arrow=True)
f.path("M170,168 Q210,90 315,80", color=MUTED, arrow=True)
f.text(430, 160, "العالِم الممارس", size=17, weight=700, color=C["blue"][0])
f.text(430, 186, "يقرأ البحث، ويقيّم ممارسته، ويتعلم من ميدانه", size=12.5, color=MUTED)
f.save("fig-1-3-scientist-practitioner.svg")

# 1-4 timeline (zig-zag, right to left) -----------------------------------------
events = [
    ("العصور الوسطى", "خرافة في أوروبا\nوبيمارستانات عربية", "slate"),
    ("1745–1826", "رش وتيوك وبينل:\nالإصلاح الإنساني", "teal"),
    ("1896", "ويتمر: أول عيادة\nنفسية في العالم", "blue"),
    ("1905", "بينيه وسيمون:\nأول مقياس للذكاء", "blue"),
    ("1917", "الحرب الأولى:\nألفا وبيتا ووودورث", "amber"),
    ("1921–1939", "رورشاخ، TAT،\nبندر، وكسلر", "amber"),
    ("1934–1960", "مصر: أول عيادة،\nعين شمس والقاهرة", "slate"),
    ("1941–1945", "الحرب الثانية:\nالأخصائي يعالج", "rose"),
    ("1947–1949", "شاكو وبولدر:\nالعالِم الممارس", "violet"),
    ("1963–1977", "كينيدي وكارتر:\nالصحة المجتمعية", "green"),
    ("1973", "مؤتمر فيل:\nالدكتوراه المهنية", "violet"),
    ("بعد 2000", "انتشار المجال\nفي قطاع غزة", "teal"),
]
f = Fig(860, 430)
f.line(30, 215, 830, 215, color=C["blue"][0], sw=3)
n = len(events)
step = 760 / (n - 1)
for k, (year, desc, c) in enumerate(events):
    x = 800 - k * step
    up = k % 2 == 0
    cy = 105 if up else 325
    f.line(x, 215, x, cy + (48 if up else -48), color=C[c][0], sw=1.5)
    f.circle(x, 215, 7, c, solid=True)
    bw = 128
    bx = min(max(x - bw / 2, 4), 860 - bw - 4)
    f.rect(bx, cy - 48, bw, 96, c)
    f.text(bx + bw / 2, cy - 28, year, size=13.5, weight=700, color=C[c][0])
    f.text(bx + bw / 2, cy + 14, desc, size=11.5)
f.text(430, 416, "تُقرأ المحطات بالترتيب الزمني من اليمين إلى اليسار", size=12, color=MUTED)
f.save("fig-1-4-timeline.svg")

# 1-5 effect size bars ---------------------------------------------------------
f = Fig(860, 300)
f.text(430, 28, "حجم أثر العلاج النفسي", size=17, weight=700, color=C["blue"][0])
base = 250
scale = 260  # px per 1.0 effect size
bars = [(560, 0.68, "سميث وجلاس (1977)\nقبل ضبط الجودة", "blue"),
        (300, 0.31, "كويبرز وزملاؤه\nبعد ضبط الجودة", "teal")]
f.line(170, base, 700, base, color=MUTED, sw=1.5)
for x, v, lab, c in bars:
    h = v * scale
    f.rect(x - 55, base - h, 110, h, c, r=4, solid=True)
    f.text(x, base - h - 16, f"≈ {v:.2f}", size=16, weight=700, color=C[c][0])
    f.text(x, base + 28, lab, size=12.5)
f.text(800, 150, "الأثر انخفض\nبعد الضبط\nلكنه بقي دالًّا", size=13, color=MUTED)
f.save("fig-1-5-effect-size.svg")
print("ch1 figures done")
