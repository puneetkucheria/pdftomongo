from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pymongo import MongoClient
import datetime
from mongodb import save_file_text

path = 'RetailPharmacyInventory.pdf'
fp = open(path, 'rb')
parser = PDFParser(fp)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize('')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
images_folder = 'images'
imagewriter = None
#outfp = StringIO()
device = PDFPageAggregator(rsrcmgr,laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
extracted_text = ''


# Process each page contained in the document.
for pagenumber, page in enumerate(doc.get_pages()):
 #   print(pagenumber)
 #   print("\n\n")
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
#        print(lt_obj.x0)
        if isinstance(lt_obj, LTTextBox):
            extracted_text = lt_obj.get_text()
            save_file_text(path,pagenumber,"LTTextBox",extracted_text,datetime.datetime.now())
        if isinstance(lt_obj, LTTextLine):
            extracted_text = lt_obj.get_text()
            if not extracted_text.strip()=='\n' and not extracted_text.strip()==' \n':
                save_file_text(path,pagenumber,"LTTextline",extracted_text,datetime.datetime.now())
