from src.manipulateColor import *
from helpers import *


def testGenerateImageGray(nameOfImage):
    image = readImage(nameOfImage)
    newImage = convertToGray(image)
    saveImage(newImage, 'manipulateColor', 'gray')


def testGenerateImageGrayWeighted(nameOfImage):
    image = readImage(nameOfImage)
    newImage = convertToGrayWeighted(image)
    saveImage(newImage, 'manipulateColor', 'grayWeighted')


def testGenerateImageIsolateChanel(nameOfImage):
    image = readImage(nameOfImage)
    newImageRed, newImageGreen, newImageBlue = isolateChanel(image)

    saveImage(newImageRed, 'manipulateColor', 'red')
    saveImage(newImageGreen, 'manipulateColor', 'green')
    saveImage(newImageBlue, 'manipulateColor', 'blue')


def testGenerateImageInverted(nameOfImage):
    image = readImage(nameOfImage)
    newImage = invertImage(image)
    saveImage(newImage, 'manipulateColor', 'inverted')


def testGenerateImageThreshold(nameOfImage, limit):
    image = readImage(nameOfImage)
    newImage = threshold(image, limit)
    saveImage(newImage, 'manipulateColor', 'threshold')


def generateAll():
    nameImage1 = "imagem-2.jpg"
    nameImage2 = "gato.jpeg"

    testGenerateImageGray(nameImage2)
    testGenerateImageGrayWeighted(nameImage2)
    testGenerateImageThreshold(nameImage1, 160)
    testGenerateImageIsolateChanel(nameImage2)
    testGenerateImageInverted(nameImage2)


generateAll()