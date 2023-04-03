from skimage import io
import cv2 as cv2


def readImage(nameOfImage):
    return io.imread('../../images/' + nameOfImage)


def convertColor(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def showImage(image):
    cv2.imshow("normal", convertColor(image))
    cv2.waitKey(0)


def saveImage(image, nameOfFolder, nameOfImage):
    cv2.imwrite('../../images_results/' + nameOfFolder + '/' + nameOfImage + '.jpg', image);


def showImageAndDestroyAll(image):
    cv2.imshow('normal', image)

    # keep image opened until ESC is pressed
    while True:
        k = cv2.waitKey(0)
        if k == 27: break
    cv2.destroyAllWindows()
