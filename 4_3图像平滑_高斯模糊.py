# LPF helps in removing noises, blurring the images etc. 低通滤波去除噪音，模糊图像
# HPF filters helps in finding edges in the images.  找到图像的边
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/lena gauss.bmp')

#方框不变，将原来每个方框的值是相等的，现在里面的值是符合高斯分布的
#方框中心的值最大，其余方框根据距离中心元素的距离递减，构成一个高斯小山包。
#原来的求平均数现在变成求加权平均数，全就是方框里的值

#窗口大小的宽和高必须是正奇数
blur = cv2.GaussianBlur(img,(5,5),0)#取0函数会根据核函数的大小自己计算沿 X，Y 方向的标准差

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

