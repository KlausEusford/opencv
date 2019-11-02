import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/Morphological Transformations.jpg')


kernel = np.ones((5,5),np.uint8)
#将内核划过图像,将内核覆盖区域的最大相素值提取，并代替锚点位置的相素。
#膨胀图与腐蚀图之差(保留物体边缘轮廓)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

#原始图像与进行开运算之后得到的图像的差
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

#进行闭运算之后得到的图像与原始图像的差。
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(gradient),plt.title('gradient')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(tophat),plt.title('tophat')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blackhat),plt.title('blackhat')
plt.xticks([]), plt.yticks([])


plt.show()