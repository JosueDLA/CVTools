import numpy as np
import cv2


class video:
    def __init__(self, path, height, width):
        self.path = path
        self.height = height
        self.width = width

    def select_video(self):
        video = cv2.VideoCapture(self.path)
        return video

    def write_video(self, output_path):
        #cv2.VideoWriter(name, codec, fps, resolution)
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')

        out = cv2.VideoWriter(output_path, fourcc, 30,
                              (self.width, self.height))
        return out
