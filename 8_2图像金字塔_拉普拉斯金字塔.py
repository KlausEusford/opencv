import cv2
import numpy as np
from matplotlib import pyplot as plt


def sameSize(img1, img2):
    rows, cols, dpt = img2.shape
    dst = img1[:rows, :cols]
    return dst

G = cv2.imread('../opencv_exercises-master/images/messi5.jpg',1)

gp = [G]
for i in range(6):
 G = cv2.pyrDown(G)
 gp.append(G) #图片6次pyrDown后加入gp数组中

lp = []
sp = []
for i in range(6, 0, -1):
 L = cv2.pyrUp(gp[i]) #图片6次pyrUp分别加入sp数组中
 sp.append(L)

 # L[i]= G[i]-pyrUp(G[i+1])
 L = cv2.subtract(gp[i - 1], sameSize(L, gp[i - 1]))  #cv2.subtract两元速相减
 lp.append(L)#拉普拉斯金字塔存放lp数组中


plt.subplot(121), plt.imshow(cv2.cvtColor(sp[-2], cv2.COLOR_BGR2RGB))
plt.title("apple"), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv2.cvtColor(lp[-1], cv2.COLOR_BGR2RGB))
plt.title("real"), plt.xticks([]), plt.yticks([])


plt.show()
