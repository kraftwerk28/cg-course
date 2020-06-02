#!/usr/bin/env python
from PIL import Image, ImageFilter
from pylab import *

FILTERS = [
    ('Original', None),
    ('Contour', ImageFilter.CONTOUR),
    ('Enchance', ImageFilter.EDGE_ENHANCE),
    ('Detail', ImageFilter.DETAIL),
    ('Enchance more', ImageFilter.EDGE_ENHANCE_MORE),
    ('Emboss', ImageFilter.EMBOSS),
    ('Find edges', ImageFilter.FIND_EDGES),
    ('Lowpass 1', ImageFilter.SMOOTH),
    ('Lowpass 2', ImageFilter.SMOOTH_MORE),
]
if __name__ == '__main__':
    img0 = Image.open('images/moon.png')
    figure(figsize=(15, 15))

    for i, finfo in enumerate(FILTERS):
        title, filter = finfo
        subplot(4, 3, i + 1)
        plt.title(title)
        filtered = img0.filter(filter) if filter else img0
        plt.imshow(filtered)
    plt.show()
