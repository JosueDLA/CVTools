import numpy as np
import cv2


def select_image(path, height, width):
    image = cv2.imread(path)
    image = cv2.resize(image, (width, height))
