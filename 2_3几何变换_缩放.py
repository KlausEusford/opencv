import cv2
import numpy as np

img = cv2.imread('../opencv_exercises-master/images/messi5.jpg')

#下面的 None 本应该是输出图像的尺寸，但是因为后边设置了缩放因子因此这里为 None
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)#原图，输出图像所需大小，fx水平轴的比例因子，fy,插值方式

#OR
#直接设置输出图像的尺寸，所以不用设置缩放因子
height, width = img.shape[:2]
res1 = cv2.resize(img,(int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_CUBIC)


cv2.imshow(u"bigger",res)
cv2.imshow(u"image",img)
cv2.imshow(u"smaller",res1)
cv2.waitKey(0)