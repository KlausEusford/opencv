import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('../opencv_exercises-master/images/image_lines.jpg')
rows,cols,ch=img.shape

pts1 = np.float32([[56,65],[368,52],[28,337],[339,330]])
pts2 = np.float32([[0,0],[200,0],[0,200],[200,200]])  #输入图像上找 4 个点，以及他们在输出图像上对应的位置，这四个点中的任意三个都不能共线。

M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()