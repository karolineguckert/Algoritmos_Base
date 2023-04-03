import matplotlib.pyplot as plt
from src.manipulateColor import *


# Function to calculate histogram
def calculateHistogram(image, channels):
    pixelCounter = [] # creates an array to count pixel values
    pixelList = [] # creates an array for 256 positions

    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    for pixel in range(0, 256):
        pixelList.append(pixel)
        pixelCount = 0
        for h in range(height):
            for w in range(width):
                for c in range(channels):
                    if image[h, w, c] == pixel:
                        pixelCount += 1
        pixelCounter.append(pixelCount)

    return pixelList, pixelCounter


# Function to plot histogram
def plotHist(r1, count1):
    plt.bar(r1, count1)
    plt.xlabel('Pixel List')
    plt.ylabel('Pixel Counter')
    plt.title('Histogram of the image')
    plt.show()


# Function to show histogram of a grayscale image
def grayscaleHistogram(image):
    image = convertToGray(image)
    pixelList, pixelCounter = calculateHistogram(image, 1)
    plotHist(pixelList, pixelCounter)


# Function to show histogram of a color image
def colorfulHistogram(image):
    pixelList, pixelCounter = calculateHistogram(image, 3)
    plotHist(pixelList, pixelCounter)