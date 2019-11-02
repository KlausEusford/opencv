import cv2
import numpy as np

img = cv2.imread('../opencv_exercises-master/images/messi5.jpg',0)
rows,cols = img.shape

M = np.float32([[0.5,0,100],[0,0.5,50]]) #0.5比例变换倍数，100横移距离

dst = cv2.warpAffine(img,M,(cols,rows)) #图，平移量，输出图像大小

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
