# To maintain the aspect ratio of an image we use thumbnail method.

from PIL import Image, ImageFilter

img = Image.open("Images_for_processing/glass.jpg")

filtered_img = img.filter(ImageFilter.SMOOTH_MORE)

filtered_img.thumbnail((400,200))
filtered_img.save("glass.png")

print(filtered_img.size)
