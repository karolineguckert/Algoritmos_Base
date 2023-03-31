from src.arithmetics import *


def testAddition():
    image1 = cv2.imread('../../images/barco.jpg')
    image2 = cv2.imread('../../images/flor.jpg')
    cv2.imshow('images', cv2.hconcat([image1, image2]))
    cv2.imshow('addition', addition(image1, 0.5, image2, 0.5))
    cv2.waitKey(0)


def testAdditionGrayScale():
    image1 = cv2.imread('../../images/barco.jpg', cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread('../../images/flor.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('images', cv2.hconcat([image1, image2]))
    cv2.imshow('addition greyscale', addition(image1, 0.5, image2, 0.5))
    cv2.waitKey(0)


def testSubtraction():
    image1 = cv2.imread('../../images/desk1.png')
    image2 = cv2.imread('../../images/desk2.png')
    cv2.imshow('images', cv2.hconcat([image1, image2]))
    cv2.imshow('subtraction', subtraction(image1, image2))
    cv2.waitKey(0)


def testSubtractionGrayScale():
    image1 = cv2.imread('../../images/desk1.png', cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread('../../images/desk2.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('images', cv2.hconcat([image1, image2]))
    cv2.imshow('subtraction greyscale', subtraction(image1, image2))
    cv2.waitKey(0)


def testMultiplication():
    image1 = cv2.imread('../../images/flor.jpg')
    image2 = cv2.imread('../../images/zeroUm.jpg')
    cv2.imshow('images', cv2.hconcat([image1, image2]))
    cv2.imshow('multiplication', multiplication(image1, image2))
    cv2.waitKey(0)


def testMultiplicationGrayScale():
    image1 = cv2.imread('../../images/flor.jpg', cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread('../../images/zeroUm.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('images', cv2.hconcat([image1, image2]))
    cv2.imshow('multiplication greyscale', multiplication(image1, image2))
    cv2.waitKey(0)


def testDivision():
    image1 = cv2.imread('../../images/desk1.png')
    image2 = cv2.imread('../../images/desk2.png')
    cv2.imshow('images', cv2.hconcat([image1, image2]))
    cv2.imshow('division', division(image1, image2))
    cv2.waitKey(0)


def testDivisionGrayScale():
    image1 = cv2.imread('../../images/desk1.png', cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread('../../images/desk2.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('images', cv2.hconcat([image1, image2]))
    cv2.imshow('division greyscale', division(image1, image2))
    cv2.waitKey(0)
