import cv2 as cv2
from skimage import io

path_img_01 = 'images/images.jpeg'
image01 = io.imread(path_img_01)
image02 = io.imread(path_img_01)
image02 = cv2.cvtColor(image02, cv2.COLOR_BGR2RGB)


image02[0] = (0, 0, 0)
cv2.imshow("imagem 02", image02)
cv2.imshow("imagem 01", image01)
cv2.waitKey(0)
