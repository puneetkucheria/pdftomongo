from mongodb import get_image_stream
from PIL import Image
import base64
from io import BytesIO

def get_img():
    #{ "_id" : ObjectId("5b9cd9f88e84031cfc877a77"), 
    path = "RetailPharmacyInventory.pdf"
    pagenumber= 0
    #layout" : "LTImage", "
    imagename="Im1"

    (image_size, image_stream) = get_image_stream(path, pagenumber, imagename)
    img = Image.frombytes('RGB', image_size, image_stream)
#    img.show()
    buffer = BytesIO()
    img.save(buffer,format="JPEG")
    img = buffer.getvalue()
    img = base64.b64encode(img)
    img_str = img.decode('ascii')
#    print(img)
    return "data:image/jpeg;base64,"+str(img_str)

if __name__ =='__main__':
    get_img()
