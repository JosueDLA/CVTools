from .frame import Frame
import numpy as np
import cv2


class Video:
    def __init__(self, path, height, width):
        self.path = path
        self.height = height
        self.width = width

    def select(self):
        video = cv2.VideoCapture(self.path)

        return video

    def read(self, video_capture):
        ret, frame = video_capture.read()
        frame = cv2.resize(frame, (self.width, self.height))

        return ret, frame

    def write(self, output_path):
        #cv2.VideoWriter(name, codec, fps, resolution)
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')

        out = cv2.VideoWriter(output_path, fourcc, 30,
                              (self.width, self.height))

        return out
