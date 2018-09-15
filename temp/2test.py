import os
import subprocess

def image_exporter(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    new_name='{}/'.format(output_dir)+pdf_path[:-4].replace(" ", "")
#    print(new_name)
    cmd = ['pdfimages', '-all', pdf_path, new_name]
#    output = []
#    output = subprocess.check_output(cmd)
    p = subprocess.run(cmd)
#    data, error = output.communicate()
    print(p.srdout.read())
#    print('Images extracted:')
#    print(os.listdir(output_dir))
#    print(p)
if __name__ == '__main__':
    pdf_path = 'RetailPharmacyInventory.pdf'
    image_exporter(pdf_path, output_dir='imagesa')
