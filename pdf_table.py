from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator, TextConverter, HTMLConverter
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
from mongodb import save_text_mongo, save_image_mongo, check_file_exist
from PIL import Image
from io import StringIO

def extract_pdf():
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    imagewriter = None
    outfp = StringIO()
    device = HTMLConverter(rsrcmgr, outfp, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''

    # Process each page contained in the document.
    for pagenumber, page in enumerate(doc.get_pages()):
        print(page.__dict__)
        interpreter.process_page(page)
#        asd = device.get_result()
#    print(output.getvalue())
#        for obj in output:
#            print(obj)

if __name__ == '__main__':
    path = 'RetailPharmacyInventory.pdf'
    extract_pdf()
