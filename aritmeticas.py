import cv2 as cv2
from skimage import io
import numpy as np

def adicao(image1, p1, image2, p2):
    if len(image1.shape) == 3:
        newImage = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)
    else:
        newImage = np.zeros((image1.shape[0], image1.shape[1], 1), np.uint8)

    for i in range(0, image1.shape[0]):  # height
        for j in range(0, image1.shape[1]):  # width
            newImage[i, j] = image1[i, j] * p1 + image2[i, j] * p2

    return newImage

def subtracao(image1, image2):
    if len(image1.shape) == 3:
        newImage = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)

        for i in range(0, image1.shape[0]):  # height
            for j in range(0, image1.shape[1]):  # width
                r1 = image1.item(i, j, 0)
                g1 = image1.item(i, j, 1)
                b1 = image1.item(i, j, 2)

                r2 = image2.item(i, j, 0)
                g2 = image2.item(i, j, 1)
                b2 = image2.item(i, j, 2)

                newImage[i, j] = [abs(r1 - r2), abs(g1 - g2), abs(b1 - b2)]
    else:
        newImage = np.zeros((image1.shape[0], image1.shape[1], 1), np.uint8)

        for i in range(0, image1.shape[0]):
            for j in range(0, image1.shape[1]):
                pixel = abs(image1.item(i, j) - image2.item(i, j))

                newImage.itemset((i, j, 0), pixel)

    return newImage

def multiplicacao(image1, image2):
    if len(image1.shape) == 3:
        newImage = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)

        for i in range(0, image1.shape[0]):  # height
            for j in range(0, image1.shape[1]):  # width
                r1 = image1.item(i, j, 0)
                g1 = image1.item(i, j, 1)
                b1 = image1.item(i, j, 2)

                r2 = image2.item(i, j, 0)
                g2 = image2.item(i, j, 1)
                b2 = image2.item(i, j, 2)

                r_result = r1 * r2
                g_result = g1 * g2
                b_result = b1 * b2

                if r_result > 255:
                    r_result = 255
                if g_result > 255:
                    g_result = 255
                if b_result > 255:
                    b_result = 255

                newImage[i, j] = [r_result, g_result, b_result]
    else:
        newImage = np.zeros((image1.shape[0], image1.shape[1], 1), np.uint8)

        for i in range(0, image1.shape[0]):
            for j in range(0, image1.shape[1]):
                pixel = image1.item(i, j) * image2.item(i, j)

                if pixel > 255:
                    pixel = 255

                newImage.itemset((i, j, 0), pixel)

    return newImage


image1 = cv2.imread('images/desk1.png',  cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('images/desk2.png',  cv2.IMREAD_GRAYSCALE)
cv2.imshow('teste1', multiplicacao(image1, image2))
cv2.waitKey(0)

