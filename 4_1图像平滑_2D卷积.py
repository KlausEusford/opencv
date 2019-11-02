# LPF helps in removing noises, blurring the images etc. 低通滤波去除噪音，模糊图像
# HPF filters helps in finding edges in the images.  找到图像的边
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/opencv_logo.png')

kernel = np.ones((5,5),np.float32)/25 #内核
#print(kernel)
dst = cv2.filter2D(img,-1,kernel) #图，目标图像的所需深度  =-1时，表示输出图像与原图像有相同的深度，卷积核

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
