from figlib import Fig, C, MUTED, INK

# 2-1 severity continuum ----------------------------------------------------
f = Fig(860, 270)
f.add('<defs><linearGradient id="g21" x1="1" x2="0"><stop offset="0" stop-color="#cfe6e2"/>'
      '<stop offset="0.5" stop-color="#f6e3c2"/><stop offset="1" stop-color="#efc6cf"/></linearGradient></defs>')
f.add('<rect x="40" y="95" width="780" height="46" rx="23" fill="url(#g21)"/>')
f.line(820, 160, 40, 160, color=MUTED, sw=1.5, arrow=True)
f.text(430, 176, "تزداد الشدة والتعطيل", size=12.5, color=MUTED)
segs = [(690, "ضغط عادي", "ردود فعل متوقعة\nللظروف"), (430, "مشكلة", "قلق امتحان، ضيق\nيمكن التعامل معه"),
        (170, "اضطراب (Disorder)", "يعطّل الحياة، تفكير\nوتوتر دائمان")]
for x, t, b in segs:
    f.text(x, 118, t, size=15, weight=700)
    f.text(x, 222, b, size=12.5)
f.pill(560, 30, 260, 40, "مجال الإرشاد النفسي", "teal")
f.pill(40, 30, 300, 40, "التحويل إلى الأخصائي أو الطبيب النفسي", "rose")
f.line(450, 50, 350, 50, color=MUTED, sw=1.5, arrow=True)
f.text(300, 255, "الفرق بين الإرشاد والعلاج فرق في الدرجة لا في النوع", size=13, color=C["blue"][0], weight=700)
f.save("fig-2-1-continuum.svg")

# 2-2 six roles ------------------------------------------------------------------
f = Fig(860, 360)
f.circle(430, 180, 78, "blue", solid=True)
f.text(430, 180, "الأخصائي النفسي\nالإكلينيكي", size=15, color="#fff", weight=700)
roles = [("الفحص النفسي", "قياس + فحص\nسلوكي ومعرفي", "teal"), ("العلاج النفسي", "فردي، أسري،\nجماعي", "violet"),
         ("إجراء البحوث", "احتياجات، انتشار،\nتقييم برامج", "amber"), ("التدريب والاستشارات", "تدريب المساعدين\nوالفرق", "green"),
         ("الإدارة والجودة", "إدارة المراكز\nوالتحسين المستمر", "slate"), ("الإسعاف النفسي الأولي", "شاهد، استمع،\nاربط", "rose")]
import math
for i, (t, b, c) in enumerate(roles):
    right = i < 3
    row = i % 3
    cx = 735 if right else 125
    cy = 62 + row * 118
    f.line(430 + (70 if right else -70), 180 + (row - 1) * 40, cx - 108 if right else cx + 108, cy, color=C[c][0], sw=1.5)
    f.card(cx - 108, cy - 48, 216, 96, t, b, color=c, tsize=14, bsize=12)
f.save("fig-2-2-six-roles.svg")

# 2-3 PFA ----------------------------------------------------------------------------
f = Fig(860, 230)
steps = [("شاهد", "Look", "تحقق من الأمان\nوالاحتياجات العاجلة", "teal"),
         ("استمع", "Listen", "استمع للمتضرر دون\nضغط أو استجواب", "blue"),
         ("اربط", "Link", "اربطه بالخدمات\nوالمعلومات وأسرته", "violet")]
x = 860 - 40 - 230
for i, (t, e, b, c) in enumerate(steps):
    dark, light = C[c]
    f.rect(x, 40, 230, 150, c)
    f.circle(x + 230 - 40, 80, 26, c, solid=True)
    f.text(x + 230 - 40, 80, str(i + 1), size=18, color="#fff", weight=700)
    f.text(x + 100, 72, t, size=20, weight=700, color=dark)
    f.text(x + 100, 98, e, size=12.5, color=MUTED)
    f.text(x + 115, 148, b, size=13)
    if i < 2:
        f.line(x - 4, 115, x - 46, 115, color=MUTED, sw=2, arrow=True)
    x -= 280
f.text(430, 215, "يقدمه أي شخص مدرَّب، وليس علاجًا متخصصًا ولا استجوابًا عن تفاصيل الحدث", size=12.5, color=MUTED)
f.save("fig-2-3-pfa.svg")

# 2-4 ethics --------------------------------------------------------------------------
f = Fig(860, 300)
eth = [("الكفاءة", "Competence", "تعرف حدودك ولا تقدم\nإلا ما تأهلت له", "blue"),
       ("الالتزام الخلقي", "Integrity", "أمانة وعدل ولا عبارات\nمضللة ولا علاقات مزدوجة", "teal"),
       ("السرية", "Confidentiality", "لا تُكسر إلا لخطر على\nالحياة وبالقدر اللازم", "rose"),
       ("احترام القيم", "Respect", "احترام المعتقدات\nوعدم التمييز", "amber"),
       ("إشراك المريض", "Participation", "إبلاغه بحقوقه وإشراكه\nفي الفحص والخطة", "violet"),
       ("تجنب العلاقات الضارة", "No harm", "لا علاقات شخصية أو مالية؛\nأحِل من تربطك به علاقة", "green")]
w, h = 262, 118
for i, (t, e, b, c) in enumerate(eth):
    col, row = i % 3, i // 3
    x = 860 - 22 - (col + 1) * w - col * 12
    y = 24 + row * (h + 22)
    dark, light = C[c]
    f.rect(x, y, w, h, c)
    f.circle(x + w - 26, y + 26, 15, c, solid=True)
    f.text(x + w - 26, y + 26, str(i + 1), size=13, color="#fff", weight=700)
    f.text(x + w / 2 - 6, y + 26, t, size=15, weight=700, color=dark)
    f.text(x + w / 2, y + 48, e, size=11, color=MUTED)
    f.text(x + w / 2, y + 86, b, size=12)
f.save("fig-2-4-ethics.svg")

# 2-5 confidentiality decision ------------------------------------------------------
f = Fig(860, 290)
f.rect(560, 20, 280, 70, "blue", solid=True)
f.text(700, 55, "معلومة عن المستفيد\nيطلبها طرف آخر أو تقلقك", size=13.5, color="#fff", weight=700)
f.rect(290, 20, 230, 70, "amber")
f.text(405, 55, "هل في الأمر خطر على حياة\nالمستفيد أو غيره؟", size=13.5, weight=700)
f.line(556, 55, 524, 55, color=MUTED, arrow=True)
f.line(405, 92, 405, 128, color=MUTED, arrow=True)
f.text(420, 112, "لا", size=13, color=MUTED, anchor="start")
f.rect(250, 132, 310, 140, "teal")
f.text(405, 158, "تبقى السرية قائمة", size=15, weight=700, color=C["teal"][0])
f.text(405, 218, "لا تُعطى إلا بتصريح كتابي يحدد:\nاسم المريض • الجهة • نوع المعلومات\n• الهدف • تاريخ انتهاء الصلاحية", size=12.5)
f.line(288, 55, 228, 55, color=MUTED, arrow=True)
f.text(258, 42, "نعم", size=13, color=MUTED)
f.rect(20, 20, 205, 252, "rose")
f.text(122, 50, "تُكسر السرية", size=15, weight=700, color=C["rose"][0])
f.text(122, 160, "أخبر المستفيد أنك ستكسر\nالسرية المتفق عليها\n\nأبلغ المختصين أو الأهل\nأو المستشفى\n\nبالقدر اللازم فقط\nلمعالجة الموقف\n\nوثّق ما فعلت", size=12.3)
f.save("fig-2-5-confidentiality.svg")

# 2-6 preparation path ----------------------------------------------------------------
f = Fig(860, 210)
steps = [("بكالوريوس", "إرشاد نفسي، طب،\nتمريض، صيدلة", "slate"),
         ("سنة علمية", "دبلوم الصحة النفسية\nالمجتمعية: الاضطرابات", "teal"),
         ("سنة عملية", "تدريب في عيادات\nبرنامج غزة", "blue"),
         ("رسالة ماجستير", "في الجامعة الإسلامية\nأو جامعة موافقة", "violet"),
         ("أخصائي نفسي إكلينيكي", "يعمل في البرنامج\nوالمؤسسات", "green")]
w = 150
x = 860 - 16 - w
for i, (t, b, c) in enumerate(steps):
    f.card(x, 40, w, 130, t, b, color=c, tsize=13.5, bsize=11.5)
    if i < 4:
        f.line(x - 2, 105, x - 18, 105, color=MUTED, arrow=True)
    x -= w + 20
f.text(430, 196, "البرنامج متوقف حاليًا بسبب الحرب", size=12, color=MUTED)
f.save("fig-2-6-path.svg")

# 2-7 tools triangle -------------------------------------------------------------------
f = Fig(860, 320)
f.add(f'<polygon points="430,40 680,270 180,270" fill="{C["blue"][1]}" stroke="{C["blue"][0]}" stroke-width="2"/>')
f.text(430, 190, "الحس الإكلينيكي\nوالخبرة", size=15, weight=700, color=C["blue"][0])
for (cx, cy, t, e, c) in [(430, 40, "المقابلة الإكلينيكية", "Clinical Interview", "teal"),
                          (690, 270, "دراسة الحالة", "Case Study", "amber"),
                          (170, 270, "الاختبارات النفسية", "Psychological Tests", "violet")]:
    f.rect(cx - 95, cy - 30, 190, 60, c, solid=True)
    f.text(cx, cy - 7, t, size=14, color="#fff", weight=700)
    f.text(cx, cy + 15, e, size=11, color="#fff")
f.text(430, 305, "لا تغني أداة عن الأخرى، ولا تكفي الاختبارات وحدها", size=12.5, color=MUTED)
f.save("fig-2-7-tools.svg")

# 2-8 team around beneficiary ------------------------------------------------------------
f = Fig(860, 380)
f.circle(430, 190, 62, "amber", solid=True)
f.text(430, 190, "المستفيد", size=17, color="#fff", weight=700)
members = [("الطبيب النفسي", "تشخيص طبي ودواء", "rose"), ("الأخصائي النفسي", "قياس وعلاج نفسي", "blue"),
           ("مدير الحالة", "تقييم أولي وتنسيق", "teal"), ("الأخصائي الاجتماعي\nوعامل PSS", "مسح وأسرة ودعم", "green"),
           ("التمريض", "أدوية ومتابعة يومية", "violet"), ("العلاج الطبيعي\nوالوظيفي", "حركة وأنشطة يومية", "slate"),
           ("التغذية والرياضة\nوالتوعية", "دعم مساند", "amber")]
n = len(members)
for i, (t, b, c) in enumerate(members):
    a = -math.pi / 2 + i * 2 * math.pi / n
    cx, cy = 430 + 315 * math.cos(a), 190 + 140 * math.sin(a)
    f.line(430 + 64 * math.cos(a), 190 + 64 * math.sin(a), cx - 70 * math.cos(a), cy - 34 * math.sin(a), color=C[c][0], sw=1.5)
    f.rect(cx - 88, cy - 34, 176, 68, c)
    f.text(cx, cy - 8 if "\n" not in t else cy - 12, t, size=12.5, weight=700, color=C[c][0])
    f.text(cx, cy + 20, b, size=11)
f.save("fig-2-8-team.svg")

# 2-9 IASC pyramid -------------------------------------------------------------------------
f = Fig(860, 360)
levels = [("4", "خدمات متخصصة", "طبيب نفسي وأخصائي: ذهان، انتحار، اضطرابات شديدة — إحالة خارجية", "rose"),
          ("3", "دعم مركّز غير متخصص", "جلسات فردية لدى الأخصائي النفسي (3–5 جلسات)", "violet"),
          ("2", "دعم المجتمع والأسرة", "توعية، مجموعات نقاش، إسعاف نفسي أولي", "teal"),
          ("1", "الخدمات الأساسية والأمان", "مأوى وغذاء وأمان وخدمات أساسية بكرامة", "blue")]
top, base_y, apex_x = 20, 330, 300
for i, (n_, t, d, c) in enumerate(levels):
    y1 = top + i * 77.5
    y2 = y1 + 77.5
    def half(y):
        return 20 + (y - top) / (base_y - top) * 230
    x1a, x1b = apex_x - half(y1), apex_x + half(y1)
    x2a, x2b = apex_x - half(y2), apex_x + half(y2)
    dark, light = C[c]
    f.add(f'<polygon points="{x1a:.0f},{y1:.0f} {x1b:.0f},{y1:.0f} {x2b:.0f},{y2:.0f} {x2a:.0f},{y2:.0f}" fill="{dark}" stroke="#fff" stroke-width="3"/>')
    f.text(apex_x, (y1 + y2) / 2, f"المستوى {n_}", size=13, color="#fff", weight=700)
    f.text(840, (y1 + y2) / 2 - 12, t, size=14, weight=700, color=dark, anchor="start")
    f.text(840, (y1 + y2) / 2 + 12, d, size=11.5, anchor="start")
    f.line(x2b + 6, (y1 + y2) / 2, 560, (y1 + y2) / 2, color=dark, sw=1, dash="3 4")
f.text(110, 345, "كلما ارتفع المستوى قلّ عدد المحتاجين وزاد التخصص", size=11.5, color=MUTED)
f.save("fig-2-9-iasc.svg")

# 2-10 pathway ------------------------------------------------------------------------------
f = Fig(860, 470)
def box(x, y, w, h, t, b, c):
    f.card(x, y, w, h, t, b, color=c, tsize=13, bsize=11.5)
box(560, 15, 280, 80, "1. الاستقبال والتقييم العام", "الأخصائي الاجتماعي في فريق MDRT", "slate")
box(560, 125, 280, 90, "2. تقييم نفسي اجتماعي أولي", "العامل النفسي الاجتماعي (100%)\n+ جلسة توعية", "teal")
f.line(700, 97, 700, 121, color=MUTED, arrow=True)
box(20, 125, 230, 80, "لا حاجة لتدخل", "يُغلق الملف بنموذج الخروج", "green")
f.line(556, 165, 254, 165, color=MUTED, arrow=True)
box(560, 250, 280, 90, "3. نقاش جماعي مفتوح", "نحو 4 جلسات (تيسير مشترك)\nأعراض خفيفة إلى متوسطة", "blue")
box(290, 250, 240, 90, "4. إحالة داخلية للأخصائي", "3–5 جلسات فردية\nالمستوى 3 (متوسط/شديد)", "violet")
box(20, 250, 240, 90, "5. إحالة خارجية", "طبيب نفسي / حماية / الأونروا\nالمستوى 4 (ذهان/انتحار)", "rose")
f.line(700, 217, 700, 246, color=MUTED, arrow=True)
f.line(620, 217, 430, 246, color=MUTED, arrow=True)
f.line(556, 295, 534, 295, color=MUTED, arrow=True)
f.line(286, 295, 264, 295, color=MUTED, arrow=True)
box(160, 375, 540, 80, "6. التقييم الختامي وإغلاق الملف", "إعادة مقياس العبء النفسي (1–10) والدعم الاجتماعي (1–10) وتوثيق SurveyCTO", "amber")
for x in (700, 410, 140):
    f.line(x, 342, max(min(x, 690), 170), 371, color=MUTED, arrow=True)
f.save("fig-2-10-pathway.svg")
print("ch2 figures done")
