import os
import sys

from PIL import Image, ImageFilter

# image_folder = sys.argv[1]
# output_folder = sys.argv[2]

#print(image_folder,output_folder)

for file in os.listdir("."):
    if file.endswith(".jpg"):
        i = Image.open(file)
        file_name,file_ext = os.path.splitext(file)
        print(file_ext)

        # i.save("/new.{}.png".format(file_name))

