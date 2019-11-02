import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_exercises-master/images/a_zhu.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #大于127取255，小于取0
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) #大于127取127，小于不变
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#大于127不变，小于取0
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
