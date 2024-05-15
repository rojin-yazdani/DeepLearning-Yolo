import numpy as np
import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

def detect_img(yolo):
    imageList = np.array(["Dataset\\1.jpg","Dataset\\2.jpg","Dataset\\3.jpg","Dataset\\4.jpg","Dataset\\5.jpg"])
    for i in imageList:
        try:
            image = Image.open(i)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    detect_img(YOLO())
