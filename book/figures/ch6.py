from figlib import Fig, C, MUTED

# 6-1 continuum ---------------------------------------------------------------
f = Fig(860, 230)
f.add('<defs><linearGradient id="g61" x1="1" x2="0"><stop offset="0" stop-color="#e9f4e7"/>'
      '<stop offset="0.5" stop-color="#fbf1e2"/><stop offset="1" stop-color="#f3d3db"/></linearGradient></defs>')
f.add('<rect x="20" y="40" width="820" height="110" rx="14" fill="url(#g61)"/>')
items = [("تمني الموت", "«ياريت أنام\nوما أصحى»"), ("فكرة انتحارية", "التفكير في إنهاء\nالحياة دون نية"),
         ("التفكير في طريقة", "كيف؟"), ("نية", "«ممكن أعملها»"), ("خطة", "تفاصيل وتوقيت"), ("سلوك", "تحضير أو محاولة")]
w = 820 / 6
for i, (t, b) in enumerate(items):
    x = 840 - w * i - w / 2
    col = [C["green"][0], C["teal"][0], C["amber"][0], C["amber"][0], C["rose"][0], C["rose"][0]][i]
    f.text(x, 72, t, size=14, weight=700, color=col)
    f.text(x, 116, b, size=11.5)
    if i < 5:
        f.line(840 - w * (i + 1) + 4, 56, 840 - w * (i + 1) - 4, 56, color=MUTED, sw=1.5, arrow=True)
f.line(780, 180, 80, 180, color=C["rose"][0], sw=3, arrow=True)
f.text(430, 205, "كلما اتجهنا يسارًا ارتفع الخطر وزادت الحاجة إلى تدخل فوري", size=12.5, color=C["rose"][0], weight=700)
f.save("fig-6-1-continuum.svg")

# 6-2 six steps -----------------------------------------------------------------
f = Fig(860, 170)
st = [("اسأل", "teal"), ("أصغِ", "blue"), ("قيّم", "violet"), ("صياغة الخطر", "amber"), ("خطة السلامة", "green"), ("أحِل وأبلغ المشرف\nوثّق وتابع", "rose")]
w = 124
x = 860 - 12 - w
for i, (t, c) in enumerate(st):
    f.circle(x + w / 2, 40, 18, c, solid=True)
    f.text(x + w / 2, 40, str(i + 1), size=14, color="#fff", weight=700)
    f.rect(x, 66, w, 74, c)
    f.text(x + w / 2, 103, t, size=13, weight=700, color=C[c][0])
    if i < 5:
        f.line(x - 2, 103, x - 14, 103, color=MUTED, arrow=True)
    x -= w + 16
f.save("fig-6-2-steps.svg")

# 6-3 safety plan ladder -----------------------------------------------------------
f = Fig(860, 400)
rungs = [("1. علامات الإنذار الخاصة بي", "أفكار، مشاعر، مواقف", "slate"),
         ("2. ما أفعله وحدي لأهدأ", "تنفس، صلاة، مشي، كتابة", "teal"),
         ("3. أماكن وأشخاص يشغلونني", "جار، مسجد، صديق", "blue"),
         ("4. من أطلب منه المساعدة", "أسماء وأرقام", "violet"),
         ("5. المختصون وخطوط الطوارئ", "الأخصائي، المؤسسة، 121", "amber"),
         ("6. جعل المحيط أكثر أمانًا", "إبعاد الوسائل بمساعدة الأسرة", "rose")]
for i, (t, b, c) in enumerate(rungs):
    y = 330 - i * 58
    x = 400 - i * 36
    f.rect(x, y, 420, 48, c)
    f.text(x + 280, y + 24, t, size=13.5, weight=700, color=C[c][0])
    f.text(x + 95, y + 24, b, size=11.5)
f.line(250, 370, 90, 50, color=C["blue"][0], sw=2.5, arrow=True)
f.text(110, 240, "نصعد درجة\nإذا لم تكفِ\nالدرجة السابقة", size=12.5, color=C["blue"][0], weight=700)
f.text(430, 392, "تُكتب بكلمات العميل، ويحتفظ بنسخة منها، وتُراجع في كل جلسة", size=12, color=MUTED)
f.save("fig-6-3-safety-plan.svg")
print("ch6 figures done")
