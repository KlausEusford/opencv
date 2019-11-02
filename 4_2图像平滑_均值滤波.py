# LPF helps in removing noises, blurring the images etc. 低通滤波去除噪音，模糊图像
# HPF filters helps in finding edges in the images.  找到图像的边
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/lena gauss.bmp')

blur = cv2.blur(img,(5,5))#均值滤波

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

