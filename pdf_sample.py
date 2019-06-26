from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("simple_table_grid.pdf", pagesize=A4, rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)
# container for the 'Flowable' objects
elements = []
styleSheet = getSampleStyleSheet()

P0 = Paragraph('''
               <b>A pa<font color=red>r</font>a<i>graph</i></b>
               <super><font color=yellow>1</font></super>''',
               styleSheet["BodyText"])
'''
data = [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', P0, '24'],
        ['30', '31', '32', '33', '34']]
'''
data = [['Fulano de Tal']]
for i in range(1, 30, 1):
    data.append([str(i) + '-06', ':', 'Name', '', '', ':', ':', '', '', '', ':'])

print(data)

t = Table(data, 11 * [0.65 * inch], 30 * [0.35 * inch])
'''
t.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                       ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                       ('VALIGN', (0, 0), (0, -1), 'TOP'),
                       ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                       ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                       ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                       ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                       ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                       ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                       ('SPAN', (1,0), (3,0))
                       ]))
'''

t.setStyle(TableStyle([
                        ('ALIGN', (0,0), (10,29), 'CENTER'),
                        ('VALIGN', (0, 0), (10, 29), 'MIDDLE'),
                        ('BOX', (0, 0), (10, 29), 0.25, colors.black),
                        ('INNERGRID', (0, 0), (10, 29), 0.25, colors.black),
                        ('SPAN', (0,0), (10,0)),
                        ('SPAN', (2,1), (4,1)),
                        ('SPAN', (7,1), (9,1))
                      ]))
#elements.append(P0)
elements.append(t)
# write the document to disk
doc.build(elements)