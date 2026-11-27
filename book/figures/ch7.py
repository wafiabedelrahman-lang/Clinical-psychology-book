import math
from figlib import Fig, C, MUTED

# 7-1 supervision functions -------------------------------------------------
f = Fig(860, 300)
f.circle(430, 140, 62, "blue", solid=True)
f.text(430, 140, "الإشراف\nالإكلينيكي", size=15, color="#fff", weight=700)
funcs = [(700, 70, "المعيارية", "الأخلاق والسياسات\nوسلامة العميل", "rose"),
         (700, 215, "التكوينية", "المعرفة والمهارة\nوتصور الحالة", "teal"),
         (160, 70, "الاستعادية", "الدعم الانفعالي\nوتجديد الطاقة", "green")]
for x, y, t, b, c in funcs:
    f.line(430 + (60 if x > 430 else -60), 140 + (y - 140) * 0.4, x + (-100 if x > 430 else 100), y, color=C[c][0], sw=1.8)
    f.card(x - 100, y - 45, 200, 90, t, b, color=c, tsize=15, bsize=12)
x, y = 160, 215
f.line(370, 160, x + 100, y, color=C["slate"][0], sw=1.5, dash="5 4")
f.rect(x - 100, y - 45, 200, 90, "slate", dash="5 4")
f.text(x, y - 22, "المؤسسية", size=14, weight=700, color=C["slate"][0])
f.text(x, y + 14, "تطوير دور المؤسسة\nلتجاوز الصعوبات الهيكلية", size=11.5)
f.text(430, 285, "الإطار المتقطع: بُعد رابع تنظيمي في مادة برنامج التدريب على الإشراف", size=11.5, color=MUTED)
f.save("fig-7-1-functions.svg")

# 7-2 Lansen rounds -----------------------------------------------------------
f = Fig(860, 290)
f.rect(40, 14, 780, 40, "slate")
f.text(430, 34, "قبل البدء: السرية وقواعد الجلسة (لا تنتقد، لا تلُم، لا تنصح)", size=13, weight=700, color=C["slate"][0])
rounds = [("1. العرض", "عرض موجز +\nسؤال الإشراف", "blue"),
          ("2. الاستيضاح", "أسئلة بلا نقد\nولا نصح", "teal"),
          ("3. مع العميل", "تماهٍ: صمت دقيقة\nثم: ماذا يشعر؟", "violet"),
          ("4. مع الأخصائي", "تماهٍ: صمت دقيقة\nثم: كيف تشعر؟", "amber"),
          ("5. تبادل الأفكار", "أفكار ونصح\nثم: ماذا كسبنا؟", "green")]
w = 148
x = 860 - 20 - w
for i, (t, b, c) in enumerate(rounds):
    f.card(x, 80, w, 130, t, b, color=c, tsize=14, bsize=12)
    if i < 4:
        f.line(x - 2, 145, x - 14, 145, color=MUTED, arrow=True)
    x -= w + 15
f.text(430, 245, "النصح ممنوع حتى الجولة الخامسة؛ والسؤال عن الشعور يفتح التأمل قبل الحلول", size=12.5, color=C["blue"][0], weight=700)
f.save("fig-7-2-lansen.svg")

# 7-3 self-care five domains ------------------------------------------------------
f = Fig(860, 330)
f.circle(430, 165, 60, "amber", solid=True)
f.text(430, 165, "الأخصائي", size=16, color="#fff", weight=700)
doms = [("الروحاني", "صلاة وذكر وتأمل", "violet"), ("الجسدي", "نوم وحركة وغذاء", "teal"),
        ("الذهني العاطفي", "كتابة يومية وامتنان", "blue"), ("نمط الحياة", "حدود بين العمل والبيت", "slate"),
        ("الدعم الاجتماعي", "أقران وأسرة وأخصائي", "green")]
for i, (t, b, c) in enumerate(doms):
    a = -math.pi / 2 + i * 2 * math.pi / 5
    cx, cy = 430 + 300 * math.cos(a), 165 + 120 * math.sin(a)
    f.line(430 + 62 * math.cos(a), 165 + 62 * math.sin(a), cx - 80 * math.cos(a), cy - 34 * math.sin(a), color=C[c][0], sw=1.5)
    f.card(cx - 95, cy - 36, 190, 72, t, b, color=c, tsize=13.5, bsize=11.5)
f.save("fig-7-3-selfcare.svg")
print("ch7 figures done")
