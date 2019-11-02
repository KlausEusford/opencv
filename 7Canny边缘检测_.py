import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/messi5.jpg',0)


#100 minVal 和 250 maxVal
#第三个参数设置用来计算图像梯度的 Sobel卷积核的大小，默认值为 3
#L2gradient用来设定求梯度大小的方程默认值为 False,使用 |Gx^2| + |Gy^2|,TURE使用√(Gx^2+Gy^2)
edges = cv2.Canny(img,100,250,4,L2gradient=False)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

#canny算法步骤
#1噪声去除用 5x5 的高斯滤波器,去除噪声
#2计算图像梯度，用 Sobel 算子计算水平方向和竖直方向的一阶导数，找到边界的梯和方向
#3非极大值抑制,对每一个像素进行检查，看这个点的梯度是不是周围具[有相同梯度方向]的点中最大的,不是取0，是下一步 ,最后会保留一条边界处最亮的一条细线
#4滞后阈值，设置两个阈值minVal 和 maxVal，高于max直接取，低于min直接舍弃，处于之间的看是否与某个被确定为真正的边界点相连