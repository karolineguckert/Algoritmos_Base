from skimage import io
import cv2 as cv


def readImage(nameOfImage):
    return io.imread('../../images/' + nameOfImage)


def convertColor(image):
    return cv.cvtColor(image, cv.COLOR_BGR2RGB)


def showImage(image):
    cv.imshow("normal", convertColor(image))
    cv.waitKey(0)


def showImageAndDestroyAll(image):
    cv.imshow('normal', image)

    # keep image opened until ESC is pressed
    while True:
        k = cv.waitKey(0)
        if k == 27: break
    cv.destroyAllWindows()
