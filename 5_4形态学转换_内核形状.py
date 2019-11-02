import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/Morphological Transformations.jpg')


kernel1 = np.ones((5,5),np.uint8)   #正方形

# 矩形：MORPH_RECT;
# 十字：MORPH_CROSS;
# 椭圆形：MORPH_ELLIPSE;

kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel4 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

print(kernel2)
print("\n")
print(kernel3)
print("\n")
print(kernel4)