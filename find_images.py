from mongodb import get_image_stream
from PIL import Image


#{ "_id" : ObjectId("5b9cd9f88e84031cfc877a77"), 
path = "RetailPharmacyInventory.pdf"
pagenumber= 0
#layout" : "LTImage", "
imagename="Im1"

(image_size, image_stream) = get_image_stream(path, pagenumber, imagename)
img = Image.frombytes('RGB', image_size, image_stream)
img.show()

