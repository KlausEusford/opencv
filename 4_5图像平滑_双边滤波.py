# LPF helps in removing noises, blurring the images etc. 低通滤波去除噪音，模糊图像
# HPF filters helps in finding edges in the images.  找到图像的边
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/lena gauss.bmp')


#空间高斯函数确保只有邻近区域的像素对中心点有影响
#灰度值相似性高斯函数确保只有与中心像素灰度值相近的才会被用来做模糊运算
#这种方法会确保边界不会被模糊掉，因为边界处的灰度值变化比较大
##9邻域直径，两个75分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

