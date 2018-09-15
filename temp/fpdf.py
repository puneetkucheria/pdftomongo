import minecart
from PIL import *

pdffile = open('RetailPharmacyInventory.pdf', 'rb')
doc = minecart.Document(pdffile)
page = doc.get_page(2)
#print(page.__dict__)
for shape in page.shapes:
#    print(shape.height)
#    print(shape.__dict__)
    print('\n')
#    print(shape.fill.color.as_rgb())
for image in page.images:
    print(image.__dict__)
    im = image.as_pil()
    print(im)
print(page.images.__dict__)
