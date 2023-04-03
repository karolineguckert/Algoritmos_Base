import cv2 as cv2
import numpy as np


# gets 2 same-sized images and 2 weights
# returns the weighted addition of the 2 images
def addition(image1, p1, image2, p2):
    rows = image1.shape[0]
    cols = image1.shape[1]
    shape_ = image1.shape

    # vhecks if the image is colorful or grayscale
    if len(shape_) == 3:
        # volorful image
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
        # grayscale image
        newImage = np.zeros((image1.shape[0], image1.shape[1], 1), np.uint8)

        for row in range(0, rows):
            for col in range(0, cols):
                pixel1 = image1.item(row, col)
                pixel2 = image2.item(row, col)

                result = pixel1 * p1 + pixel2 * p2

                newImage.itemset((row, col, 0), result)

    return newImage


# gets 2 same-sized images
# returns the difference between image1 and image2
def subtraction(image1, image2):
    rows = image1.shape[0]
    cols = image1.shape[1]
    shape_ = image1.shape

    img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # checks if the image is colorful or grayscale
    if len(shape_) == 3:
        # colorful image
        newImage = np.zeros((rows, cols, 3), np.uint8)

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

                # if pixel in image2 is different from pixel in image1 use pixel drom image2
                if b_result != 0 and g_result != 0 and r_result != 0:
                    newImage.itemset((row, col, 0), image2.item(row, col, 0))
                    newImage.itemset((row, col, 1), image2.item(row, col, 1))
                    newImage.itemset((row, col, 2), image2.item(row, col, 2))
    else:
        # grayscale image
        newImage = np.zeros((rows, cols, 1), np.uint8)
        for row in range(0, rows):
            for col in range(0, cols):
                pixel1 = image1.item(row, col)
                pixel2 = image2.item(row, col)

                result = abs(pixel1 - pixel2)

                newImage.itemset((row, col, 0), result)

    return newImage


# gets 2 same-sized images
# returns the multiplication of image1 and image2
def multiplication(image1, image2):
    rows = image1.shape[0]
    cols = image1.shape[1]
    shape_ = image1.shape
    
    # checks if the image is colorful or grayscale
    if len(shape_) == 3:
        # colorful image
        newImage = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)

        for row in range(0, rows):
            for col in range(0, cols):
                r_img1 = image1.item(row, col, 0)
                g_img1 = image1.item(row, col, 1)
                b_img1 = image1.item(row, col, 2)

                r_img2 = image2.item(row, col, 0)
                g_img2 = image2.item(row, col, 1)
                b_img2 = image2.item(row, col, 2)

                r_result = r_img1 * r_img2
                g_result = g_img1 * g_img2
                b_result = b_img1 * b_img2

                # checks for overflow
                if r_result > 255:
                    r_result = 255
                if g_result > 255:
                    g_result = 255
                if b_result > 255:
                    b_result = 255

                newImage.itemset((row, col, 0), r_result)
                newImage.itemset((row, col, 1), g_result)
                newImage.itemset((row, col, 2), b_result)
    else:
        # grayscale image
        newImage = np.zeros((image1.shape[0], image1.shape[1], 1), np.uint8)
        for row in range(0, rows):
            for col in range(0, cols):
                pixel1 = image1.item(row, col)
                pixel2 = image2.item(row, col)

                result = pixel1 * pixel2

                newImage.itemset((row, col, 0), result)

    return newImage

# gets 2 same-sized images
# returns the division of image1 and image2
def division(image1, image2):
    rows = image1.shape[0]
    cols = image1.shape[1]
    shape_ = image1.shape

    # checks if the image is colorful or grayscale
    if len(shape_) == 3:
        # colorful image
        newImage = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)

        for row in range(0, rows):
            for col in range(0, cols):
                r_img1 = 1 if image1.item(row, col, 0) == 0 else image1.item(row, col, 0)
                g_img1 = 1 if image1.item(row, col, 1) == 0 else image1.item(row, col, 1)
                b_img1 = 1 if image1.item(row, col, 2) == 0 else image1.item(row, col, 2)

                r_img2 = 1 if image2.item(row, col, 0) == 0 else image2.item(row, col, 0)
                g_img2 = 1 if image2.item(row, col, 1) == 0 else image2.item(row, col, 1)
                b_img2 = 1 if image2.item(row, col, 2) == 0 else image2.item(row, col, 2)

                r_result = r_img1 / r_img2
                g_result = g_img1 / g_img2
                b_result = b_img1 / b_img2

                newImage.itemset((row, col, 0), r_result)
                newImage.itemset((row, col, 1), g_result)
                newImage.itemset((row, col, 2), b_result)
    else:
        # grayscale image
        newImage = np.zeros((image1.shape[0], image1.shape[1], 1), np.uint8)
        for row in range(0, rows):
            for col in range(0, cols):
                pixel1 = 1 if image1.item(row, col) == 0 else image1.item(row, col)
                pixel2 = 1 if image2.item(row, col) == 0 else image2.item(row, col)

                result = pixel1 / pixel2

                newImage.itemset((row, col, 0), result)

    return newImage
