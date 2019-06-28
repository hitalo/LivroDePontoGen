# encoding: utf-8
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak


class PDFGen:

    elements = []

    def create_new_document(self, rows, data_model, data):

        name = data_model.name
        month = data_model.month
        day1 = data_model.day1
        vacations = data_model.vacations

        self.doc = SimpleDocTemplate("pdfs/" + name + ".pdf", pagesize=A4, rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)

        # how much for saturday, assuming (0 - monday, 6 - sunday)
        diff = (6 - day1)

        data.sort()
        for name in data:

            data_table = self.make_table(name, rows, month, vacations, diff)

            t = Table(data_table, 11 * [0.65 * inch], (rows + 2) * [0.33 * inch])
            t.setStyle(TableStyle(self.get_table_style(rows, vacations, diff)))

            self.elements.append(t)
            self.elements.append(PageBreak())






    def make_table(self, name, rows, month, vacations, diff):

        data_table = [[name.decode('cp1252').encode('utf-8')]]
        data_table.append(["Data", 'Entrada', 'Assinatura', '', '', 'Saída', 'Entrada', 'Assinatura', '', '', 'Saída'])
        for i in range(1, rows + 1, 1):

            if (i % 7 == diff): # saturday
                data_table.append(["{:02d}".format(i) + '-' + "{:02d}".format(month), ':', 'SÁBADO', '', '', ':', ':', 'SÁBADO', '', '', ':'])
            elif (i % 7 == diff + 1 or (diff == 6 and i % 7 == 0)):  # sunday
                data_table.append(["{:02d}".format(i) + '-' + "{:02d}".format(month), ':', 'DOMINGO', '', '', ':', ':', 'DOMINGO', '', '', ':'])
            elif(i in vacations):
                data_table.append(["{:02d}".format(i) + '-' + "{:02d}".format(month), ':', 'FERIADO', '', '', ':', ':', 'FERIADO', '', '', ':'])
            else:
                data_table.append(["{:02d}".format(i) + '-' + "{:02d}".format(month), ':', '', '', '', ':', ':', '', '', '', ':'])

        return data_table






    def get_table_style(self, rows, vacations, diff):
        # default
        table_style = [
            ('ALIGN', (0, 0), (10, rows+1), 'CENTER'),
            ('VALIGN', (0, 0), (10, rows+1), 'MIDDLE'),
            ('BOX', (0, 0), (10, rows+1), 0.25, colors.black),
            ('INNERGRID', (0, 0), (10, rows+1), 0.25, colors.black),
            ('SPAN', (0, 0), (10, 0)),
            ('SPAN', (2, 1), (4, 1)),
            ('SPAN', (7, 1), (9, 1))
        ]

        # big cells for names
        for i in range(1, rows+2, 1):
            table_style.append(('SPAN', (2, i), (4, i)))
            table_style.append(('SPAN', (7, i), (9, i)))


        # different color for saturdays and sundays
        for i in range(1, rows + 1, 1):
            if (i in vacations or i % 7 == diff  or i % 7 == diff + 1 or (diff == 6 and i % 7 == 0)):
                table_style.append(('BACKGROUND', (0, i+1), (11, i+1), colors.gray))

        return table_style





    def build(self):
        self.doc.build(self.elements)