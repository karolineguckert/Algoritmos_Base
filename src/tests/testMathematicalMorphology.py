from helpers import *
from src.manipulateColor import *
from src.mathematicalMorphology import *


def testGenerateImageErosion(nameOfImage, kernel):
    image = readImage(nameOfImage)
    newImage = erosion(image, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'erosion')


def testGenerateImageDilation(nameOfImage, kernel):
    image = readImage(nameOfImage)
    newImage = dilation(image, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'dilation')


def testGenerateImageOpening(nameOfImage, kernel):
    image = readImage(nameOfImage)
    newImage = opening(image, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'opening')


def testGenerateImageClosing(nameOfImage, kernel):
    image = readImage(nameOfImage)
    newImage = closing(image, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'closing')


def testGenerateImageConvolution(nameOfImage, kernel):
    image = readImage(nameOfImage)
    image = convertToGrayWeighted(image)
    newImage = convolution(image, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'convolution')

def testLimitExternal(nameOfImage, kernel):
    image = readImage(nameOfImage)
    gray = convertToGray(image)
    newImage = limitExternal(gray, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'external limits')


def testLimitInternal(nameOfImage, kernel):
    image = readImage(nameOfImage)
    gray = convertToGray(image)
    newImage = limitInternal(gray, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'internal limits')


def generateAll():
    nameImage1 = 'j.png'
    nameImage2 = 'gato.jpeg'
    kernel_5x5 = np.ones([5, 5], np.uint8)
    kernelConvolution = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    testGenerateImageErosion(nameImage1, kernel_5x5)
    testGenerateImageDilation(nameImage1, kernel_5x5)
    testGenerateImageOpening(nameImage1, kernel_5x5)
    testGenerateImageClosing(nameImage1, kernel_5x5)
    testGenerateImageConvolution(nameImage2, kernelConvolution)


def testLimits():
    nameImage1 = 'bob.jpg'
    kernel = np.ones([2, 2], np.uint8)

    testLimitExternal(nameImage1, kernel)
    testLimitInternal(nameImage1, kernel)


testLimits()
generateAll()
