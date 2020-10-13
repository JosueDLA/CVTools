import numpy as np
import cv2


class Frame(np.ndarray):
    def __new__(cls, frame, height, width):
        obj = np.asarray(frame).view(cls)
        obj.height = height
        obj.width = width
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.heigh = getattr(obj, 'height', None)
        self.width = getattr(obj, 'width', None)

    def filter_frame(height, width):
        """
        Filter frame with multiple techniques to make contour detection easier.
        """

        # GrayScale the frame
        gray = cv2.cvtColor(image, cv2.COLOR_BAYER_GR2GRAY)

        # White frame for outpur contour video
        self.create_white_frame()

        # Edge detection with blured image
        blured = cv2.GaussianBlur(gray, (5, 5), 0)
        #bilateral = cv2.bilateralFilter(gray, 11, 17, 17)
        canny = cv2.Canny(blurred, 40, 200)

        # Dilate lines for earsier contour detection
        kernel = np.ones((3, 3), np.uint8)
        dilated = cv2.dilate(canny, kernel, iterations=2)

    def get_contours(self):
        pass

    def create_white_frame(self):
        white_frame = 0 * np.ones((self.height, self.width, 3), np.uint8)

        return white_frame
