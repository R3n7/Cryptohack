from PIL import Image, ImageChops

def get_xor(image_1, image_2):

    i1 = ImageChops.invert(image_1)
    i2 = ImageChops.invert(image_2)

    return ImageChops.invert(ImageChops.add(ImageChops.subtract(i2, i1), ImageChops.subtract(i1, i2)))

im1 = Image.open('/home/kali/Downloads/abstract.png')
im2 = Image.open('/home/kali/Downloads/nautilus.jpg')
im3 = (get_xor(im1,im2))
im3.show()