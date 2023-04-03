from helpers import *
from mathematicalMorphology import *


def testGenerateErosion(nameOfImage, kernel):
    image = readImage(nameOfImage)
    newImage = erosion(image, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'erosion')


def testGenerateDilation(nameOfImage, kernel):
    image = readImage(nameOfImage)
    newImage = dilation(image, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'dilation')


def testGenerateOpening(nameOfImage, kernel):
    image = readImage(nameOfImage)
    newImage = opening(image, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'opening')


def testGenerateClosing(nameOfImage, kernel):
    image = readImage(nameOfImage)
    newImage = closing(image, kernel)
    saveImage(newImage, 'mathematicalMorphology', 'closing')


def generateAll():
    nameImage1 = 'j.png'
    kernel_5x5 = np.ones([5, 5], np.uint8)

    testGenerateErosion(nameImage1, kernel_5x5)
    testGenerateDilation(nameImage1, kernel_5x5)
    testGenerateOpening(nameImage1, kernel_5x5)
    testGenerateClosing(nameImage1, kernel_5x5)


generateAll()
