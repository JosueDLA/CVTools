from . import contour
import numpy as np
import cv2


class Frame(np.ndarray):
    def __new__(cls, frame, height, width):

        frame = cv2.resize(frame, (width, height))

        obj = np.asarray(frame).view(cls)
        obj.height = height
        obj.width = width
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.height = getattr(obj, 'height', None)
        self.width = getattr(obj, 'width', None)

    def filter_frame(self):
        """
        Filter frame with multiple techniques to make contour detection easier.
        """

        # GrayScale the frame
        gray = cv2.cvtColor(self, cv2.COLOR_BGR2GRAY)

        # White frame for outpur contour video
        white = self.create_white_frame()

        # Edge detection with blured image
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        #bilateral = cv2.bilateralFilter(gray, 11, 17, 17)
        canny = cv2.Canny(blurred, 20, 40)

        # Dilate lines for earsier contour detection
        kernel = np.ones((3, 3), np.uint8)
        dilated = cv2.dilate(canny, kernel, iterations=2)

        return white, dilated

    def get_contours(self, dilated):
        (contours, hierarchy) = cv2.findContours(
            dilated.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        hierarchy = hierarchy[0]

        contours, hierarchy = contour.remove_parent_contour(
            contours, hierarchy)

        return contours, hierarchy

    def create_white_frame(self):
        white_frame = 0 * np.ones((self.height, self.width, 3), np.uint8)

        return white_frame
