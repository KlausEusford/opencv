import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/messi5.jpg',1)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#高斯金字塔顶部图像中的每个像素值等于下一层图像中 5 个像素的高斯加权平均值

#函数 cv2.pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金子塔（尺寸变小，分辨率降低）
lower_reso = cv2.pyrDown(img)
lower_reso2 = cv2.pyrDown(lower_reso)
#函数 cv2.pyrUp() 从一个低分辨率小尺寸的图像向下构建一个金子塔（尺寸变大，但分辨率不会增加）
higher_reso = cv2.pyrUp(lower_reso2)
higher_reso2 = cv2.pyrUp(higher_reso)

cv2.imshow("1",img)
cv2.imshow("2",lower_reso)
cv2.imshow("3",lower_reso2)
cv2.imshow("4",higher_reso)
cv2.imshow("5",higher_reso2)

cv2.waitKey(0)

#一旦使用 cv2.pyrDown()，图像的分辨率就会降低，信息就会被丢失

