import cv2 as cv
import numpy as np


# Function to convert a color image to grayscale
# using arithmetic method
def convertToGray(image):
    auxImage = np.zeros((image.shape[0], image.shape[1], 1), np.uint8)  # create a new image with 1 channel

    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    for i in range(height):
        for j in range(width):
            # sum all the color values and multiply to 0.33 to convert to grayscale
            auxImage[i, j] = sum(image[i, j]) * 0.33

    cv.imshow("grayscale - arithmetic", auxImage)

    return auxImage


# Function to convert a color image to grayscale
# using weighted method
def convertToGrayWeighted(image):
    auxImage = np.zeros((image.shape[0], image.shape[1], 1), np.uint8)  # create a new image with 1 channel

    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    for i in range(height):
        for j in range(width):
            # get the color of each color channel in the pixel specified
            (r, g, b) = image[i, j]

            # multiply each color channel and sum all the values to convert to grayscale
            auxImage[i, j] = (r * float(0.299) + g * float(0.587) + b * float(0.114))

    cv.imshow("grasycale - weighted", auxImage)


# Function to isolate the channels of the image
def isolateChanel(image):
    auxImageRed = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)  # create a new image with 1 channel
    auxImageGreen = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)  # create a new image with 1 channel
    auxImageBlue = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)  # create a new image with 1 channel

    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    for i in range(height):
        for j in range(width):
            # get the color of each color channel in the pixel specified
            (b, g, r) = image[i, j]

            auxImageRed[i, j] = (0, 0, r)  # takes just the red pixel and makes others get 0
            auxImageGreen[i, j] = (0, g, 0)  # takes just the green pixel and makes others get 0
            auxImageBlue[i, j] = (b, 0, 0)  # takes just the blue pixel and makes others get 0

    cv.imshow("isolate chanel red-", auxImageRed)
    cv.imshow("isolate chanel green-", auxImageGreen)
    cv.imshow("isolate chanel blue-", auxImageBlue)


# Function to invert the image
def invertImage(image):
    auxImage = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)  # create a new image with 1 channel

    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    for i in range(height):
        for j in range(width):
            auxImage[i, j] = 255 - image[i, j]  # subtract the possible maximum value of the pixel value

    cv.imshow("inverted -", auxImage)


# Function to threshold the image
def threshold(image, limit):
    grayImage = convertToGray(image)  # convert image to gray
    auxImage = np.zeros((grayImage.shape[0], grayImage.shape[1], 3), np.uint8)  # create a new image with 1 channel

    height = grayImage.shape[0]  # takes the number of columns
    width = grayImage.shape[1]  # takes the number of lines

    for i in range(height):
        for j in range(width):
            if grayImage[i, j][0] > limit:
                auxImage[i, j] = 255
            else:
                auxImage[i, j] = 0

    cv.imshow("threshold -", auxImage)
