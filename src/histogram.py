import matplotlib.pyplot as plt
from manipulateColor import *


# Function to show histogram for a grayscale image
def histogramGrayscale(image, imageGray):
    # openCv builtIn function to calculate histogram
    # params: image, channels (0 because is grayscale), mask (NONE to find histogram for full image),
    # histogram size (256 for full scale), range
    hist = cv.calcHist([imageGray], [0], None, [256], [0, 256])

    plt.hist(image.ravel(), 256, [0, 256])  # function to plot histogram
    plt.title('Histogram for grayscale image')
    plt.show()


# Function to show histogram for a color image
def histogramColor(image):
    color = ('b', 'g', 'r')
    for channel, col in enumerate(color):
        # channel param = r, g or b
        histr = cv.calcHist([image], [channel], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.title('Histogram for color scale image')
    plt.show()


# Function to show an equalized image
def equalizeHistogram(image):
    img = image
    imgToYuv = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # transform bgr to yuv
    imgToYuv[:, :, 0] = cv.equalizeHist(imgToYuv[:, :, 0])  # openCv method to equalize
    histEqualizationResult = cv.cvtColor(imgToYuv, cv.COLOR_YUV2BGR)  # transform back to bgr

    cv.imwrite('images_results/histogramEqResult.jpg', histEqualizationResult)

