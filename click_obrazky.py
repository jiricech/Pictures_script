from pathlib import Path
from PIL import Image
import os
import click
#from PIL import Imagefilter  NEFUNGUJE IMPORT!!!
# image=Image.open(r"C:\Users\ingji\Desktop\pictures\road.jpg")
# image.show()
#@click.command()#dekorator zabali funkci process, command cimz oznacime tu funkci jako command, ktery se ma zpracovavat na prikazove radce.

size_300=(500,500)
def process():

    """Zpracuje obrazky."""
    for pictures_path in Path().glob('./*.jpg'):
        img=Image.open(pictures_path)
        img=img.rotate(0)
        img.thumbnail(size_300)
        #img=img.filter(Imagefilter.GaussianBlur(radius=8))
        img.save('./output/{}'.format(pictures_path.name))

        print('done {}'.format(pictures_path))

process()
# for kitten_path in Path().glob("pictures/*.jpg"):
#     img=Image.open(kitten_path)
#     img=img.rotate(20)
#     img=img.filter(Imagefilter.GaussianBlur(radius=8))
#     img.save("/output"/{}.format(kitten_path.name))
#
#     print("done{}".format(kitten_path))