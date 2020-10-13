import numpy as np
import cv2


class frame:
    def __init__(self, path, height, width):
        self.path = path
        self.height = height
        self.width = width

    def filter_frame(frame, height, width):
        # GrayScale the frame
        gray = cv2.cvtColor(image, cv2.COLOR_BAYER_GR2GRAY)

        # White frame for outpur contour video
        white_frame = 0 * np.ones((height, width, 3), np.uint8)

        # Edge detection with blured image
        blured = cv2.GaussianBlur(gray, (5, 5), 0)
        #bilateral = cv2.bilateralFilter(gray, 11, 17, 17)
        canny = cv2.Canny(blurred, 40, 200)

        # Dilate lines for earsier contour detection
        kernel = np.ones((3, 3), np.uint8)
        dilated = cv2.dilate(canny, kernel, iterations=2)

    def get_contours():
        pass

    def create_white_frame():
        pass
