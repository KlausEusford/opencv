import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/gradient.jpg',0)
#Scharr和Sobel算子求一阶导数，图像中的边缘区域像素值会发生“跳跃”，对这些像素求导，在其一阶导数在边缘位置为极值。
#如果 ksize=-1，会使用 3x3 的 Scharr 滤波器,3x3滤波器时Scharr滤波器比3x3的 Sobel 滤波器好
#x方向Scharr 滤波器卷积核[[-3 0 3 ]    #y方向Scharr 滤波器卷积核[[-3 -10 -3]
#                       [-10 0 10]    #                       [0   0   0]
#                       [-3 0 3]]     #                       [3   10  3]]


# Laplacian 算子可假设其离散实现类似于二阶 Sobel 导数,如果对像素值求二阶导数，边缘处二阶导数为0
# 如果 ksize=1，会使用 3x3 的 Laplacian 滤波器
# 3x3卷积核[[0 1 0]
#          [1 -4 1]
#          [0 1 0]]

#第二参数表示所求图像的深度，-1表与原图像相同，Sobel建立的图像位数不够，会有截断。因此要使用16位有符号的数据类型，即cv2.CV_16S
laplacian1 = cv2.Laplacian(img,cv2.CV_64F,ksize=1)
laplacian=cv2.convertScaleAbs(laplacian1) # 转回uint8


sobelx_ = cv2.Sobel(img,-1,1,0,ksize=1)  #深度如果使用-1只会求导数为正的，而不会求图像由亮到暗的负导数
sobelx1 = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1) #1，0表示在x，y方向求导的阶数，0表示这个方向上没有求导。
sobelx=cv2.convertScaleAbs(sobelx1)


sobely1 = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1) #ksize表示算子的大小，必须为1、3、5、7
sobely=cv2.convertScaleAbs(sobely1)
#or
abs_sobel = np.absolute(sobely1) #取绝对值
sobel_8u = np.uint8(abs_sobel)


dst = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)


plt.subplot(3,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,2),plt.imshow(laplacian1,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,3),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,4),plt.imshow(sobelx_,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,5),plt.imshow(sobelx1,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,6),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,7),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,8),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,9),plt.imshow(dst,cmap = 'gray')
plt.title('dst'), plt.xticks([]), plt.yticks([])
plt.show()
