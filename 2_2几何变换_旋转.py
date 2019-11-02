import cv2
import numpy as np

img = cv2.imread('../opencv_exercises-master/images/messi5.jpg',0)
rows,cols = img.shape


M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1) #第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子

dst = cv2.warpAffine(img,M,(cols,rows)) #M就是个变换矩阵

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
