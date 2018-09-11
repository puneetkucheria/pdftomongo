from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator 
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
from pymongo import MongoClient
import datetime
import os
from io import StringIO
from binascii import b2a_hex
from PIL import Image

connection = MongoClient()

def write_file (folder, filename, filedata, flags='w'):
    #Write the file data to the folder and filename combination
    #(flags: 'w' for write text, 'wb' for write binary, use 'a' instead of 'w' for append)
    result = False
    if os.path.isdir(folder):
        try:
            file_obj = open(os.path.join(folder, filename), flags)
            file_obj.write(filedata)
            file_obj.close()
            result = True
        except IOError:
            pass
        return result

def determine_image_type (stream_first_4_bytes):
    #Find out the image file type based on the magic number comparison of the first 4 (or 2) bytes
    file_type = None
    bytes_as_hex = b2a_hex(stream_first_4_bytes)
    if str(bytes_as_hex).startswith('ffd8'):
        file_type = '.jpeg'
        print("found jpeg")
    elif bytes_as_hex == '89504e47':
        file_type = ',png'
        print("found png")
    elif bytes_as_hex == '47494638':
        file_type = '.gif'
        print("found gif")
    elif str(bytes_as_hex).startswith('424d'):
        file_type = '.bmp'
        print("found bmp")
    else:
        file_type = '.jpeg'
        print("filetype not found")
    return file_type





def save_image (lt_image, page_number, images_folder):
    #Try to save the image data from this LTImage object, and return the file name, if successful
    result = None
    if lt_image.stream:
        file_stream = lt_image.stream.get_data()
#        file_stream = lt_image.bits
#        print(str(lt_image.x0)+' '+str(lt_image.y0))
#        print(str(lt_image.x1)+' '+str(lt_image.y1))
#        print(lt_image.)
        (x0,y0,x1,y1) = lt_image.bbox
        print(x0)
        print(y0)
        print(x1)
        print(y1)

        (width, height) = lt_image.srcsize
        print('height: '+str(height)+'      width :'+str(width)+'    image name:'+str(lt_image.name))
        file_ext = determine_image_type(file_stream[0:4])
        print(file_ext)
        if file_ext:
            file_name = ''.join([str(page_number), '_', lt_image.name, file_ext])
            if write_file(images_folder, file_name, file_stream, flags='wb'):
                result = file_name
                print("image saved"+result)
    return result



def save_file_text(path, page, layout, text, date):
    db = connection.db_pdftomongo.col_text_dump
    post = {'file':path, 'pagenumber':page, 'layout':layout, 'text':text, 'createdon':date}
    print(post)
#    post_id = db.insert_one(post).inserted_id



def find_images_in_obj(outer_layout, pagenumber, images_folder):
    print('infigure')
    for thing in outer_layout:
        print('thing found')
        print(thing)
        if isinstance(thing, LTImage):
            save_image(thing, pagenumber, images_folder)




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
outfp = StringIO()
device = PDFPageAggregator(rsrcmgr,laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
extracted_text = ''


# Process each page contained in the document.
for pagenumber, page in enumerate(doc.get_pages()):
    print(pagenumber)
    print("\n\n")
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
#        print(lt_obj.x0)
#        if isinstance(lt_obj, LTTextBox):
#            extracted_text = lt_obj.get_text()
#            save_file_text(path,pagenumber,"LTTextBox",extracted_text,datetime.datetime.now())
#        if isinstance(lt_obj, LTTextLine):
#            extracted_text = lt_obj.get_text()
#            if not extracted_text==' \n' and not extracted_text=='\n':
#                save_file_text(path,pagenumber,"LTTextline",extracted_text,datetime.datetime.now()) 
        if isinstance(lt_obj, LTFigure):
            print('found figure')
            find_images_in_obj(lt_obj, pagenumber, images_folder)
        if isinstance(lt_obj, LTImage):
#            print(b2hex(lt_obj))
            print('x0 ='+str(lt_obj.x0))
            save_image(lt_obj,pagenumber, images_folder)
