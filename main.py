import cv2 as cv
from skimage import io


def convertToGray(image):
    auxImage = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    height = image.shape[0]
    width = image.shape[1]

    for i in range(height):
        for j in range(width):
            (r, g, b) = image[i, j]
            auxImage[i, j] = r * float(0.299) + g * float(0.587) + b * float(0.114)
    cv.imshow("grayscale 1", auxImage)


def convertToGrayWeighted(image):
    auxImage = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    height = image.shape[0]
    width = image.shape[1]

    for i in range(height):
        for j in range(width):
            (r, g, b) = image[i, j]
            auxImage[i, j] = (r * float(0.299) + g * float(0.587) + b * float(0.114)) / 3
    cv.imshow("grasycale weighted", auxImage)


def main():
    path_img_01 = 'images/images.jpeg'
    image01 = io.imread(path_img_01)
    image02 = io.imread(path_img_01)
    image02 = cv.cvtColor(image02, cv.COLOR_BGR2RGB)

    convertToGray(image02)
    convertToGrayWeighted(image02)
    # cv.imshow("imagem 02", image02)
    cv.imshow("imagem 01", image01)
    cv.waitKey(0)


main()
