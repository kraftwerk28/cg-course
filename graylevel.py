#!/usr/bin/env python
from PIL import Image
from pylab import *

if __name__ == '__main__':
    img = Image.open('images/profile.png').convert('L')
    im = array(img)
    gray()
    im2 = 255 - im
    im3 = (100. - 255) * im + 100
    im4 = 255. * (im / 255.) ** 2
    imshow(im4)
    show()
