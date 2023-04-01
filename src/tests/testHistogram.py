from src.histogram import *
from helpers import *


def testHistogram(nameOfImage):
    image = readImage(nameOfImage)

    colorfulHistogram(image)
    grayscaleHistogram(image)

    showImageAndDestroyAll(image)

testHistogram('imagem-2.jpg')
testHistogram('ave-03.jpeg')