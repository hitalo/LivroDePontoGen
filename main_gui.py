import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from data_model import DataModel

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Gerar Livro de Ponto")

        self.set_border_width(10)
        self.set_resizable(False)
        self.month = 0
        self.day1 = 0

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        month_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        day1_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        leapyear_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        name_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        vbox.pack_start(name_box, True, True, 0)
        vbox.pack_start(month_box, True, True, 0)
        vbox.pack_start(leapyear_box, True, True, 0)
        vbox.pack_start(day1_box, True, True, 0)
        vbox.pack_start(button_box, True, True, 0)

        label_name = Gtk.Label("Nome: ")
        name_box.pack_start(label_name, False, False, True)


        self.name_entry = Gtk.Entry()
        name_box.pack_start(self.name_entry, False, False, True)


        label_month = Gtk.Label("Mês: ")
        month_box.pack_start(label_month, False, False, True)


        month_combo = Gtk.ComboBoxText()
        month_combo.connect("changed", self.on_month_combo_changed)
        month_combo.set_entry_text_column(0)
        for month in range(1, 13, 1):
            month_combo.append_text(str(month))

        month_box.pack_start(month_combo, False, False, True)

        self.label_leapyear = Gtk.Label("Ano bissexto? ")
        self.label_leapyear.set_sensitive(False)
        leapyear_box.pack_start(self.label_leapyear, False, False, True)

        self.check_leapyear = Gtk.CheckButton()
        self.check_leapyear.set_sensitive(False)
        leapyear_box.pack_start(self.check_leapyear, False, False, True)


        label_day1 = Gtk.Label("Dia 1 será: ")
        day1_box.pack_start(label_day1, False, False, 0)


        days = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        day1_combo = Gtk.ComboBoxText()
        day1_combo.connect("changed", self.on_day1_combo_changed)
        day1_combo.set_entry_text_column(0)
        for day in days:
            day1_combo.append_text(day)

        day1_box.pack_start(day1_combo, False, False, 0)



        button = Gtk.Button.new_with_label("Gerar pdf")
        button.connect("clicked", self.create_pdf)
        button_box.pack_start(button, True, True, 0)

        self.add(vbox)




    def on_month_combo_changed(self, combo):
        self.month = combo.get_active()

        if(self.month == 1):
            self.check_leapyear.set_sensitive(True)
            self.label_leapyear.set_sensitive(True)
        else:
            self.check_leapyear.set_sensitive(False)
            self.label_leapyear.set_sensitive(False)



    def on_day1_combo_changed(self, combo):
        self.day1 = combo.get_active()


    def create_pdf(self, button):
        data_model = DataModel()

        data_model.name = self.name_entry.get_text()
        data_model.month = self.month
        data_model.is_leapyear = self.check_leapyear.get_active()
        data_model.day1 = self.day1


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()