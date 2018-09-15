from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
from mongodb import save_text_mongo, save_image_mongo, check_file_exist
from PIL import Image

def save_image (lt_image, page_number):
    #Try to save the image data from this LTImage object, and return the file name, if successful
    result = None
    if lt_image.stream:
        file_stream = lt_image.stream.get_data()
        img = Image.frombytes('RGB', lt_image.srcsize, file_stream)
        if img:
            file_name = ''.join([images_folder,'/',path[:-4],'_',str(page_number+1), '_', lt_image.name, '.png'])
            print(file_name)
            img.save(file_name)
    return result

def convert_image (image_size, image_stream):
    img = Image.frombytes('RGB', image_size, image_stream)
    return img

def find_images_in_obj(outer_layout, pagenumber):
    for lt_obj in outer_layout:
        if isinstance(lt_obj, LTImage):
#            save_image(thing, pagenumber)
            save_image_mongo(path, pagenumber, 'LTImage', lt_obj.name, lt_obj.srcsize, lt_obj.stream.get_data())
def extract_pdf():
    #path = 'RetailPharmacyInventory.pdf'
    print(check_file_exist(path))
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    #images_folder = 'images'
    imagewriter = None
    #outfp = StringIO()
    device = PDFPageAggregator(rsrcmgr,laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''

    # Process each page contained in the document.
    for pagenumber, page in enumerate(doc.get_pages()):
    #    print(page.__dict__)
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox):
                extracted_text = lt_obj.get_text()
                save_text_mongo(path,pagenumber,"LTTextBox",extracted_text)
            if isinstance(lt_obj, LTTextLine):
                extracted_text = lt_obj.get_text()
                if not extracted_text==' \n' and not extracted_text=='\n':
                    save_text_mongo(path,pagenumber,"LTTextline",extracted_text)
            if isinstance(lt_obj, LTFigure):
    #            print(lt_obj.__dict__)
    #            print('\n')
                find_images_in_obj(lt_obj, pagenumber)
            if isinstance(lt_obj, LTImage):
    #            save_image(lt_obj,pagenumber)
                save_image_mongo(path, pagenumber, 'LTImage', lt_obj.name, lt_obj.srcsize, lt_obj.stream.get_data())

if __name__ == '__main__':
    path = 'RetailPharmacyInventory.pdf'
    images_folder = 'images'
    extract_pdf()

