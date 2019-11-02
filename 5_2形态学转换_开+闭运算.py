import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/opening.jpg')
img1 = cv2.imread('../opencv_exercises-master/images/closing.jpg')

kernel = np.ones((5,5),np.uint8)
#开运算，先腐蚀再膨胀，去白噪声
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#闭运算，填充前景物体中的小洞，或者前景物体上的小黑点
closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(opening),plt.title('opening')
plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(img1),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(closing),plt.title('closing')
plt.xticks([]), plt.yticks([])

plt.show()