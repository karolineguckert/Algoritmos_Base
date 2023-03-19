import cv2 as cv
from skimage import io
import numpy as np

#Function to convert a color image to grayscale
#using arithmetic method
def convertToGray(image):
    auxImage = np.zeros((image.shape[0], image.shape[1], 1), np.uint8) #create a new image with 1 channel

    height = image.shape[0] #takes the number of columns
    width = image.shape[1]  #takes the number of lines

    for i in range(height):
        for j in range(width):

            #sum all the color values and multiply to 0.33 to convert to grayscale
            auxImage[i, j] = sum(image[i, j]) * 0.33

    cv.imshow("grayscale - arithmetic", auxImage)

#Function to convert a color image to grayscale
#using weighted method
def convertToGrayWeighted(image):
    auxImage = np.zeros((image.shape[0], image.shape[1], 1), np.uint8) #create a new image with 1 channel

    height = image.shape[0] #takes the number of columns
    width = image.shape[1]  #takes the number of lines

    for i in range(height):
        for j in range(width):
            #get the color of each color channel in the pixel specified
            (r, g, b) = image[i, j]

            # multiply each color channel and sum all the values to convert to grayscale
            auxImage[i, j] = (r * float(0.299) + g * float(0.587) + b * float(0.114))

    cv.imshow("grasycale - weighted", auxImage)


def

def main():
    path_img_01 = 'images/images.jpeg'

    image02 = io.imread(path_img_01)

    cv.imshow("normal", image02)

    convertToGray(image02)
    convertToGrayWeighted(image02)

    cv.waitKey(0)


main()
