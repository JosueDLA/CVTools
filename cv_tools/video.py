import numpy as np
import cv2


def select_video(path, height, width):
    video = cv2.VideoCapture(path)

    #cv2.VideoWriter(name, codec, fps, resolution)
    fourcc = cv2.VideoWriter(*'MPEG')
    out = cv2.VideoWriter('output.avi', fourcc, 30, (width, height))

    return video, out
