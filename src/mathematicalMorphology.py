import numpy as np


# Function to erosion the image
def erosion(image, kernel):
    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    resultImage = np.zeros([height, width, 4], np.uint8)

    start = int(len(kernel) / 2)  # initial position
    widthKernel = len(kernel)  # takes the number of lines
    heightKernel = len(kernel[0])  # takes the number of columns

    for i in range(start, width - start):  # lines
        for j in range(start, height - start):  # columns
            pixelImage = image[j][i]  # get pixel of the image

            countKernel = 0  # reset counter of not nullables in kernel
            countAll = 0  # reset counter of not nullables in original image and kernel

            for k in range(0, widthKernel):  # lines
                for l in range(0, heightKernel):  # columns
                    pixelKernel = kernel[k][l]

                    # count how many values are not nullables in kernel
                    if pixelKernel != 0:
                        countKernel += 1

                        positionLine = i - start + k  # get line position of pixel
                        positionColumn = j - start + l  # get column position of pixel

                        # count how many values are not nullables int kernel and original image
                        if image[positionColumn][positionLine][0] != 0:
                            countAll += 1

            # if counters have the same quantities of not nullables change de pixel
            if countKernel == countAll:
                resultImage[j][i] = pixelImage

    return resultImage


# Function to dilation the image
def dilation(image, kernel):
    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    resultImage = np.zeros([height, width, 4], np.uint8)

    start = int(len(kernel) / 2)  # initial position
    row_element = len(kernel)  # takes the number of lines
    col_element = len(kernel[0])  # takes the number of columns

    for i in range(start, width - start):  # lines
        for j in range(start, height - start):  # columns
            pixelImage = image[j][i]  # get pixel of the image

            if pixelImage[0] != 0:
                for k in range(0, row_element):  # lines
                    for l in range(0, col_element):  # columns
                        pixelKernel = kernel[k][l]

                        positionLine = i - start + k  # get line position of pixel
                        positionColumn = j - start + l  # get column position of pixel

                        # if pixelKernel equals 1 change the pixel
                        if pixelKernel == 1:
                            resultImage[positionColumn][positionLine] = pixelImage

    return resultImage


# Function to opening the image
def opening(image, kernel):
    imageErosion = erosion(image, kernel)
    return dilation(imageErosion, kernel)


# Function to closing the image
def closing(image, kernel):
    imageDilation = dilation(image, kernel)
    return erosion(imageDilation, kernel)