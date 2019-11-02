import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/Morphological Transformations.jpg')

#如果与卷积核对应的原图像的所有像素值都是 1，那么中心元素就保持原来的像素值，否则就变为零
kernel = np.ones((4,4),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)  #iteration的值越高，模糊程度(腐蚀程度)就越高 呈正相关关系

#与卷积核对应的原图像的像素值中只要有一个是 1，中心元素的像素值就是 1
dilation = cv2.dilate(img,kernel,iterations = 1)

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(erosion),plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(dilation),plt.title('dilation')
plt.xticks([]), plt.yticks([])
plt.show()