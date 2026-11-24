from figlib import Fig, C, MUTED

# 3-1 forms spectrum -------------------------------------------------------------
f = Fig(860, 250)
f.add('<defs><linearGradient id="g31" x1="1" x2="0"><stop offset="0" stop-color="#1f5f7a"/>'
      '<stop offset="1" stop-color="#2b7f78"/></linearGradient></defs>')
f.add('<rect x="40" y="112" width="780" height="14" rx="7" fill="url(#g31)" opacity="0.85"/>')
forms = [(700, "المقننة", "Structured", "أسئلة ثابتة بترتيبها\nأعلى ثباتًا وأسهل مقارنة", "blue"),
         (430, "شبه المقننة", "Semi-structured", "مجالات محددة وصياغة حرة\nالأكثر شيوعًا", "violet"),
         (160, "الحرة", "Unstructured", "بلا أسئلة محددة\nأقرب إلى بناء الثقة", "teal")]
for x, t, e, b, c in forms:
    f.circle(x, 119, 13, c, solid=True)
    f.text(x, 40, t, size=17, weight=700, color=C[c][0])
    f.text(x, 66, e, size=12, color=MUTED)
    f.text(x, 175, b, size=12.5)
f.line(560, 225, 300, 225, color=MUTED, arrow=True)
f.text(430, 210, "كلما اتجهنا يسارًا زادت حرية الأخصائي وقلّ التقنين", size=12, color=MUTED)
f.save("fig-3-1-forms.svg")

# 3-2 stages -----------------------------------------------------------------------
f = Fig(860, 230)
st = [("الإعداد", "هدف · مكان\nوقت · استعداد", "slate", False),
      ("الافتتاح", "علاقة وثقة\nوحدود السرية", "teal", True),
      ("الجزء الرئيسي", "جمع المعلومات\nوفحصها", "blue", True),
      ("الختام", "تلخيص\nوخطوة تالية", "violet", True),
      ("التدخل", "عند الحاجة\nللحالة", "amber", False),
      ("التوثيق", "بعد خروج\nالمفحوص", "green", False)]
w = 128
x = 860 - 12 - w
for i, (t, b, c, core) in enumerate(st):
    f.card(x, 50, w, 120, t, b, color=c, tsize=13.5, bsize=11.5)
    if i < 5:
        f.line(x - 2, 110, x - 12, 110, color=MUTED, arrow=True)
    x -= w + 14
f.add(f'<rect x="{860 - 12 - 4 * w - 3 * 14 - 6}" y="36" width="{3 * w + 2 * 14 + 12}" height="148" rx="12" fill="none" stroke="{C["blue"][0]}" stroke-width="1.5" stroke-dasharray="5 5"/>')
f.text(430, 24, "الجلسة نفسها: ثلاث مراحل كبرى", size=13, weight=700, color=C["blue"][0])
f.text(430, 205, "تتطور العلاقة من الجلسة الأولى إلى العاشرة؛ فلا تتوقع كل شيء في اللقاء الأول", size=12, color=MUTED)
f.save("fig-3-2-stages.svg")

# 3-3 question types ------------------------------------------------------------------
f = Fig(860, 300)
f.pill(330, 16, 200, 44, "أنواع الأسئلة", "blue")
groups = [(720, "الوظيفية", "تمهيد واتصال\nعبور\nضبط واستفسار", "teal"),
          (500, "الأساسية", "مفتوحة / مغلقة\nمباشرة / غير مباشرة\nإيحائية (بحذر)", "violet"),
          (280, "الدائرية", "سؤال طرف ثالث عن\nتصوره لتفاعل اثنين\n(مدرسة ميلانو)", "amber"),
          (90, "الافتراضية\nوالموقفية", "«لنفترض أن…»\nفي الانتقاء المهني", "rose")]
for x, t, b, c in groups:
    f.path(f"M430,60 C430,90 {x},80 {x},108", color=C[c][0], sw=1.6)
    f.card(x - 95, 110, 190, 150, t, b, color=c, tsize=14, bsize=12)
f.text(430, 285, "الهدف: السؤال أداة لتسهيل الطريق إلى المعلومة، لا لتوجيه الإجابة", size=12.5, color=MUTED)
f.save("fig-3-3-questions.svg")

# 3-4 Gazda staircase ---------------------------------------------------------------------
f = Fig(860, 330)
steps = [("1. التيسير", "ماذا عندك؟\nثقة + شكوى واضحة", "احترام · تعاطف · دفء", "teal"),
         ("2. الانتقالية", "هل أنت مستعد؟\nمشكلة محددة + قبول المسؤولية", "عيانية · أصالة · إفصاح عن الذات", "violet"),
         ("3. الفعل", "هيا نجرّب الحل\nخطة + قرار + تجريب", "مواجهة · فورية (هنا والآن)", "amber")]
for i, (t, b, sk, c) in enumerate(steps):
    x = 860 - 30 - (i + 1) * 260
    y = 220 - i * 80
    dark, light = C[c]
    f.rect(x, y, 255, 316 - y, c, r=8)
    f.add(f'<rect x="{x}" y="{y}" width="255" height="34" rx="8" fill="{dark}"/>')
    f.text(x + 127, y + 17, t, size=15, color="#fff", weight=700)
    f.text(x + 127, (y + 34 + 296) / 2, b, size=12)
    f.text(x + 127, 300, sk, size=11.5, color=dark, weight=700)
f.text(700, 90, "لا ننتقل إلى الدرجة التالية\nقبل أن يتحقق هدف الدرجة\nالتي نقف عليها", size=12.5, color=MUTED)
f.line(30, 322, 830, 322, color=MUTED, sw=1)
f.text(560, 322 - 8, "", size=1)
f.save("fig-3-4-gazda.svg")

# 3-5 empathy spectrum ----------------------------------------------------------------------
f = Fig(860, 230)
items = [(700, "العطف (الشفقة)", "ينظر إليه من أعلى: «يا حرام!»\nيشعر المفحوص بالضعف", "rose"),
         (430, "التعاطف", "«أفهم ما تشعر به وأقف معك»\nمع بقاء المسافة المهنية", "green"),
         (160, "التماهي (التوحد)", "يذوب في مشاعره ويتألم مثله\nيفقد القدرة على المساعدة", "rose")]
f.line(60, 110, 800, 110, color=MUTED, sw=2)
for x, t, b, c in items:
    dark, light = C[c]
    f.rect(x - 125, 40, 250, 140, c, solid=(c == "green"))
    col = "#fff" if c == "green" else dark
    f.text(x, 70, t, size=16, weight=700, color=col)
    f.text(x, 128, b, size=12, color="#fff" if c == "green" else "#1d2a3a")
f.text(430, 210, "قريب بما يكفي لتفهم، وبعيد بما يكفي لتساعد", size=13, color=C["green"][0], weight=700)
f.save("fig-3-5-empathy.svg")

# 3-6 concreteness scale ------------------------------------------------------------------------
f = Fig(860, 200)
x0, x1 = 780, 80
for i in range(11):
    x = x0 - i * (x0 - x1) / 10
    shade = int(230 - i * 15)
    color = f"rgb({min(255, 160 + i * 8)},{shade},{shade})"
    f.add(f'<rect x="{x - 30}" y="60" width="60" height="44" fill="{color}" stroke="#fff" stroke-width="2"/>')
    f.text(x, 82, str(i), size=15, weight=700)
f.text(x0, 125, "لا شيء", size=12, color=MUTED)
f.text(x1, 125, "أشد ما يكون", size=12, color=MUTED)
x7 = x0 - 7 * (x0 - x1) / 10
f.add(f'<path d="M{x7},56 l-9,-16 h18 z" fill="{C["rose"][0]}"/>')
f.text(x7, 28, "«حزني الآن 7»", size=14, weight=700, color=C["rose"][0])
f.text(430, 165, "نعيد السؤال في الجلسات التالية لنرى التغير: 7 ثم 5 ثم 3…", size=13, color=C["blue"][0], weight=700)
f.save("fig-3-6-concreteness.svg")

# 3-7 confrontation balance -----------------------------------------------------------------------
f = Fig(860, 230)
f.line(80, 120, 780, 120, color=MUTED, sw=3)
pts = [(720, "التهرب من الواقع", "يرى التناقض ويسكت عنه\nفيُحرم المفحوص من الاستبصار", "slate"),
       (430, "مواجهة متوازنة", "تصف التناقض بهدوء\nوتحفظ الكرامة وتذكّر بالقدرات", "green"),
       (140, "هجوم جارح", "«أنت تكذب!»\nيدفع المفحوص إلى الدفاع", "rose")]
for x, t, b, c in pts:
    f.circle(x, 120, 14 if c == "green" else 10, c, solid=True)
    f.text(x, 80, t, size=15, weight=700, color=C[c][0])
    f.text(x, 170, b, size=12)
f.text(430, 215, "المواجهة تحتاج رصيدًا من الثقة؛ مكانها الجلسات المتقدمة", size=12.5, color=MUTED)
f.save("fig-3-7-confrontation.svg")

# 3-8 iceberg --------------------------------------------------------------------------------------
f = Fig(860, 360)
f.add('<rect x="0" y="110" width="860" height="250" fill="#e6f0f5"/>')
f.line(0, 110, 860, 110, color=C["blue"][0], sw=2)
f.text(830, 98, "خط الماء", size=11.5, color=C["blue"][0], anchor="start")
f.add(f'<polygon points="430,20 500,110 360,110" fill="#ffffff" stroke="{C["blue"][0]}" stroke-width="2"/>')
f.text(430, 80, "الكلمات", size=14, weight=700, color=C["blue"][0])
f.add(f'<polygon points="362,110 498,110 740,330 120,330" fill="#ffffff" fill-opacity="0.7" stroke="{C["blue"][0]}" stroke-width="2"/>')
below = ["تعبيرات الوجه · الابتسامة · العينان · الدمعة",
         "حركات اليدين والرجلين · الجلسة",
         "نبرة الصوت · علوّه · سرعته · الصمت",
         "العادات الحركية: النقر، العبث بالشعر والأظافر",
         "استعمال الوقت: النظر المتكرر إلى الساعة"]
for i, s in enumerate(below):
    f.text(430, 145 + i * 38, s, size=12.5)
f.text(120, 60, "ما نسمعه\nفوق الماء", size=12.5, color=MUTED)
f.text(120, 230, "ما نلاحظه\nإن انتبهنا", size=12.5, color=MUTED)
f.save("fig-3-8-iceberg.svg")

# 3-9 error sources ------------------------------------------------------------------------------------
f = Fig(860, 320)
f.circle(430, 160, 62, "blue", solid=True)
f.text(430, 160, "دقة\nالمقابلة", size=16, color="#fff", weight=700)
src = [("1. المفحوص", "دافعيته وذاكرته\nوانفعاله", "rose", 690, 60),
       ("2. الأخصائي", "مهارته وتحيزاته\nوحالته", "violet", 690, 160),
       ("3. العلاقة بينهما", "دفء أو برود\nأو تحدٍّ", "teal", 690, 260),
       ("4. المعلومات المطلوبة", "نوع الأسئلة\nوصياغتها", "amber", 170, 60),
       ("5. ظروف المقابلة", "المكان والوقت\nوالغرض", "slate", 170, 160),
       ("6. تقدّم المعرفة", "حدود ما نعرفه\nاليوم", "green", 170, 260)]
for t, b, c, x, y in src:
    f.line(430 + (62 if x > 430 else -62), 160 + (y - 160) * 0.5, x + (-100 if x > 430 else 100), y, color=C[c][0], sw=1.5)
    f.card(x - 100, y - 42, 200, 84, t, b, color=c, tsize=13, bsize=11.5)
f.save("fig-3-9-errors.svg")
print("ch3 figures done")
