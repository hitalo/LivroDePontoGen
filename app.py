from pdf_gen import PDFGen
from data_manager import DataManager

data_manager = DataManager()

doc = PDFGen()
doc.create_new_document(31, 6, 2, data_manager.get_names())
doc.build()