from helpers import *
from mathematicalMorphology import *
from manipulateColor import *


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


generateAll()
