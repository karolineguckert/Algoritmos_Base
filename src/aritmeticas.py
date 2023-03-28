import cv2 as cv2
import numpy as np


def addition(image1, p1, image2, p2):
    rows = image1.shape[0]
    cols = image1.shape[1]
    shape_ = image1.shape

    if len(shape_) == 3:
        newImage = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)

        for row in range(0, rows):
            for col in range(0, cols):
                b_img1 = image1.item(row, col)
                g_img1 = image1.item(row, col)
                r_img1 = image1.item(row, col)

                b_img2 = image2.item(row, col)
                g_img2 = image2.item(row, col)
                r_img2 = image2.item(row, col)

                b_result = b_img1 * p1 + b_img2 * p2
                g_result = g_img1 * p1 + g_img2 * p2
                r_result = r_img1 * p1 + r_img2 * p2

                newImage.itemset((row, col, 0), b_result)
                newImage.itemset((row, col, 1), g_result)
                newImage.itemset((row, col, 2), r_result)
    else:
        newImage = np.zeros((image1.shape[0], image1.shape[1], 1), np.uint8)

        for row in range(0, rows):
            for col in range(0, cols):
                pixel1 = image1.item(row, col)
                pixel2 = image2.item(row, col)

                result = pixel1 * p1 + pixel2 * p2

                newImage.itemset((row, col, 0), result)

    return newImage


# recebe duas imagens com mesmas dimensões (cores - BGR)
# retorna a diferença (imagem BGR)
def subtraction(image1, image2):
    rows = image1.shape[0]
    cols = image1.shape[1]
    shape_ = image1.shape

    img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    if len(shape_) == 3:
        image_diff = np.zeros((rows, cols, 3), np.uint8)

        for row in range(0, rows):
            for col in range(0, cols):
                b_img1 = img1.item(row, col)
                g_img1 = img1.item(row, col)
                r_img1 = img1.item(row, col)

                b_img2 = img2.item(row, col)
                g_img2 = img2.item(row, col)
                r_img2 = img2.item(row, col)

                b_result = abs(b_img1 - b_img2)
                g_result = abs(g_img1 - g_img2)
                r_result = abs(r_img1 - r_img2)

                if b_result != 0 and g_result != 0 and r_result != 0:
                    image_diff.itemset((row, col, 0), image2.item(row, col, 0))
                    image_diff.itemset((row, col, 1), image2.item(row, col, 1))
                    image_diff.itemset((row, col, 2), image2.item(row, col, 2))
    else:
        image_diff = np.zeros((rows, cols, 1), np.uint8)
        for row in range(0, rows):
            for col in range(0, cols):
                pixel1 = image1.item(row, col)
                pixel2 = image2.item(row, col)

                result = abs(pixel1 - pixel2)

                image_diff.itemset((row, col, 0), result)

    return image_diff


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


image1 = cv2.imread('images/desk1.png', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('images/desk2.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('teste1', multiplicacao(image1, image2))
cv2.waitKey(0)
