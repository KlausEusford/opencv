# LPF helps in removing noises, blurring the images etc. 低通滤波去除噪音，模糊图像
# HPF filters helps in finding edges in the images.  找到图像的边
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/lena sp.bmp')


#用与卷积框对应像素的中值来替代中心像素的值，去除椒盐噪声
#前面的滤波器都是用计算得到的一个新值来取代中心像素的值，而中值滤波是用中心像素周围（也可以使他本身）的值来取代他。
#卷积核的大小也应该是一个奇整数。
median = cv2.medianBlur(img,9)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

