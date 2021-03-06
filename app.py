# encoding: utf-8
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from data_model import DataModel
from pdf_gen import PDFGen
from data_manager import DataManager

class App:

    def __init__(self, master):

        self.data_model = DataModel()
        self.is_leapyear = IntVar()

        frame = Frame(master)
        frame.grid(row=0, columnspan=3, sticky='W', padx=50, pady=20, ipadx=20, ipady=20)

        frame.grid_columnconfigure(0, weight=1, uniform="foo")
        frame.grid_columnconfigure(1, weight=4, uniform="foo")

        name_lb = Label(frame, text="Nome:")
        name_lb.grid(row=0, column=0, sticky='E', pady=10)

        self.name_en = Entry(frame, bd =5)
        self.name_en.grid(row=0, column=1, columnspan=2, sticky="WE", pady=3)


        month_lb = Label(frame, text="Mês:")
        month_lb.grid(row=1, column=0, sticky='E', pady=10)

        months = []
        for month in range(1, 13, 1):
            months.append(str(month))

        self.month_cb = ttk.Combobox(frame, values=months)
        self.month_cb.grid(row=1, column=1, columnspan=1, sticky="W", pady=10)
        self.month_cb.bind("<<ComboboxSelected>>", self.check_leap)

        self.leapyear_chk = Checkbutton(frame, text="Ano Bissexto?", state=DISABLED, variable=self.is_leapyear)
        self.leapyear_chk.grid(row=1, column=2, columnspan=1, pady=10, sticky='W')

        day1 = Label(frame, text="Dia 1 será:")
        day1.grid(row=2, column=0, sticky='E', pady=10)

        days = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

        self.day1_cb = ttk.Combobox(frame, values=days)
        self.day1_cb.grid(row=2, column=1, columnspan=1, sticky="WE", pady=10)

        vacations_lb = Label(frame, text="Feriados (Números separados por vírgula):")
        vacations_lb.grid(row=3, column=0, columnspan=3, sticky='WE', pady=10)

        self.vacations_en = Entry(frame, bd=5)
        self.vacations_en.grid(row=4, column=0, columnspan=3, sticky="WE", pady=3)

        pdf_bt = Button(frame, text="Gerar PDF", command=self.create_pdf)
        pdf_bt.grid(row=5, column=0, columnspan=3, pady=(30,5))


    def create_pdf(self):
        self.data_model.name = self.name_en.get().strip()
        self.data_model.month = self.month_cb.get().strip()
        self.data_model.is_leapyear = self.is_leapyear.get()
        self.data_model.day1 = self.day1_cb.current()
        self.data_model.vacations = []

        if self.vacations_en.get():
            self.data_model.vacations = self.vacations_en.get().replace(" ", "").split(',')

        if(self.validate()):

            if (self.data_model.month == 2):
                days = 28
                if (self.data_model.is_leapyear):
                    days += 1
            elif (self.data_model.month in [1, 3, 5, 7, 8, 10, 12]):
                days = 31
            else:
                days = 30


            data_manager = DataManager()

            doc = PDFGen()
            doc.create_new_document(days, self.data_model, data_manager.get_names())
            doc.build()

            messagebox.showinfo("Concluído", "PDF gerado")

        else:
            messagebox.showerror("Erro", "Dados inválidos")



    def validate(self):

        try:
            self.data_model.month = int(self.data_model.month)
        except ValueError:
            return False

        try:
            self.data_model.day1 = int(self.data_model.day1)
        except ValueError:
            return False

        if self.data_model.vacations:
            try:
                self.data_model.vacations = [int(x) for x in self.data_model.vacations]
            except ValueError:
                return False


        if not (self.data_model.name):
            return False
        elif not (self.data_model.month < 13 and self.data_model.month > 0):
            return False
        elif not (self.data_model.day1 < 7 and self.data_model.day1 > -1):
            return False
        else:
            return True


    def check_leap(self, event):
        if(self.month_cb.current() == 1):
            self.leapyear_chk['state'] = 'normal'
        else:
            self.leapyear_chk['state'] = 'disabled'


root = Tk()
root.title("Gerar Livro de Ponto")
app = App(root)
root.mainloop()