from src.manipulateColor import *
from helpers import *


def testGenerateImageGray(nameOfImage):
    image = readImage(nameOfImage)
    convertToGray(image)
    showImage(image)


def testGenerateImageGrayWeighted(nameOfImage):
    image = readImage(nameOfImage)
    convertToGrayWeighted(image)
    showImage(image)


def testGenerateImageIsolateChanel(nameOfImage):
    image = readImage(nameOfImage)
    isolateChanel(image)
    showImage(image)


def testGenerateImageInverted(nameOfImage):
    image = readImage(nameOfImage)
    invertImage(image)
    showImage(image)


def testGenerateImageThreshold(nameOfImage, limit):
    image = readImage(nameOfImage)
    threshold(image, limit)
    showImage(image)

testGenerateImageThreshold("imagem-2.jpg", 160)