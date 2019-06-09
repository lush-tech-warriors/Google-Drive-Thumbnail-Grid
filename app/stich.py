from __future__ import print_function
import os
import glob
from PIL import Image

def generate(dir):
    files = glob.glob(dir + '/*')
    resultHeight = int(round(len(files) / 8 * 100))
    result = Image.new("RGB", (800, resultHeight))

    for index, file in enumerate(files):
      path = os.path.expanduser(file)
      img = Image.open(path)
      img.thumbnail((100, 100), Image.ANTIALIAS)
      x = index // 2 * 100
      y = index % 2 * 100
      w, h = img.size
      print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
      result.paste(img, (x, y, x + w, y + h))

    result.save(os.path.expanduser(dir + 'result.jpg'))