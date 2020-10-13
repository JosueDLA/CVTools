import numpy as np
import cv2


class Image:
    def __init__(self, path, height, width):
        self.path = path
        self.height = height
        self.width = width

    def select(self):
        image = cv2.imread(self.path)
        image = cv2.resize(image, (self.width, self.height))

        return image
