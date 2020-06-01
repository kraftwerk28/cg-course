#!/usr/bin/env python
from os import path
import math
import numpy as np
from PIL import Image
import scipy.misc

if __name__ == '__main__':
    location = 'images/chestxray.jpg'
    img = Image.open(location)
    b = scipy.misc.fromimage(img)

    gamma = .5

    b1 = b.astype(float)
    b3 = np.max(b1)
    b2 = b1 / b3
    b3 = numpy.log(b2) * gamma
    c = np.exp(b3) * 255.
    c1 = scipy.misc.fromimage(c)
    img.show(c1)
