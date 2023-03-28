from src.arithmetics import *


def testAddition():
    image1 = cv2.imread('images/barco.jpg')
    image2 = cv2.imread('images/flor.jpg')
    cv2.imshow('images', cv2.hconcat(image1, image2))
    cv2.imshow('addition', addition(image1, 0.5, image2, 0.5))
    cv2.waitKey(0)


def testAdditionGrayScale():
    image1 = cv2.imread('images/barco.jpg', cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread('images/flor.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('images', cv2.hconcat(image1, image2))
    cv2.imshow('addition', addition(image1, 0.5, image2, 0.5))
    cv2.waitKey(0)
