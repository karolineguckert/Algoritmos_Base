from src.histogram import *
from helpers import *


def testHistogram(nameOfImage):
    image = readImage(nameOfImage)
    imageGray = convertToGray(image)

    histogramGrayscale(image, imageGray)
    histogramColor(image)
    equalizeHistogram(imageGray)

    showImageAndDestroyAll(image)


testHistogram('imagem-2.jpg')

