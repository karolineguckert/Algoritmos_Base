import cv2 as cv
from skimage import io
import numpy as np

def convertToGray(image):
    auxImage = np.zeros((image.shape[0], image.shape[1], 1), np.uint8)
    height = image.shape[0]
    width = image.shape[1]

    for i in range(height):
        for j in range(width):

            auxImage[i, j] = sum(image[i, j]) * 0.33

    cv.imshow("grayscale - arithmetic", auxImage)


def convertToGrayWeighted(image):
    auxImage = np.zeros((image.shape[0], image.shape[1], 1), np.uint8)

    height = image.shape[0]
    width = image.shape[1]

    for i in range(height):
        for j in range(width):
            (r, g, b) = image[i, j]
            auxImage[i, j] = (r * float(0.299) + g * float(0.587) + b * float(0.114))
    cv.imshow("grasycale - weighted", auxImage)


def main():
    path_img_01 = 'images/images.jpeg'

    image02 = io.imread(path_img_01)

    cv.imshow("normal", image02)

    convertToGray(image02)
    convertToGrayWeighted(image02)

    cv.waitKey(0)


main()
