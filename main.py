import cv2 as cv
from skimage import io

def convertImageToGray(image01):
    print("a")

    image03 = cv.cvtColor(image01, cv.COLOR_BGR2RGB)

    for i in range(0, image01.shape[0]):
        for j in range(0, image01.shape[1]):
            pixel01 = image01[i, j]
            pixel02 = 0.299 * pixel01[0] + 0.587 * pixel01[1] + 0.114 * pixel01[2]
            image03[i,j] = pixel02

    cv.imshow(image03)

def convert2Gray(image):
    img = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            (r, g, b) = image[i, j]

            img[i, j] = (r*float(0.299) + g*float(0.587) + b*float(0.114))
    cv.imshow("grayscale 1", img)


def convert2GrayWeighted(image):
    img = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            (r, g, b) = image[i, j]

            img[i, j] = (r*float(0.299) + g*float(0.587) + b*float(0.114))/3
    cv.imshow("grasycale weighted", img)



def main():
    path_img_01 = 'images/images.jpeg'
    image01 = io.imread(path_img_01)
    image02 = io.imread(path_img_01)
    image02 = cv.cvtColor(image02, cv.COLOR_BGR2RGB)

    convert2Gray(image02)
    convert2GrayPonderada(image02)
    #cv.imshow("imagem 02", image02)
    cv.imshow("imagem 01", image01)
    cv.waitKey(0)

main()