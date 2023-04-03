from src.arithmetics import *


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
    widthKernel = len(kernel)  # takes the number of lines
    heightKernel = len(kernel[0])  # takes the number of columns

    for i in range(start, width - start):  # lines
        for j in range(start, height - start):  # columns
            pixelImage = image[j][i]  # get pixel of the image

            if pixelImage[0] != 0:
                for k in range(0, widthKernel):  # lines
                    for l in range(0, heightKernel):  # columns
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


# Function to convolution the image
def convolution(image, kernel):
    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    resultImage = np.zeros([height, width, 3], np.uint8)

    start = int(len(kernel) / 2)  # initial position
    widthKernel = len(kernel)  # takes the number of lines
    heightKernel = len(kernel[0])  # takes the number of columns

    for i in range(start, width - start):  # lines
        for j in range(start, height - start):  # columns
            pixelValue = 0

            for k in range(0, widthKernel):  # lines
                for l in range(0, heightKernel):  # columns
                    positionLine = i - start + k  # get line position of pixel
                    positionColumn = j - start + l  # get column position of pixel

                    pixel = image[positionColumn][positionLine]
                    pixelValue += pixel[0] * kernel[k][l]

            if pixelValue < 0:
                resultImage[j][i] = 0
            elif pixelValue > 255:
                resultImage[j][i] = 255
            else:
                resultImage[j][i] = pixelValue

    return resultImage


# Function to apply roberts method
def roberts(image):
    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    kernel_gx = np.array([[0, 1], [-1, 0]])  # Gx
    kernel_gy = np.array([[1, 0], [0, -1]])  # Gy

    resultImage = np.zeros((height, width, 1), np.uint8)

    for i in range(0, width - 1):  # lines
        for j in range(0, height - 1):  # columns
            pixel_gy = 0  # reset gy of pixel
            pixel_gx = 0  # reset gx of pixel

            for k in range(0, 2):
                for l in range(0, 2):
                    pixel_gx += kernel_gx[k][l] * image[j + l][i + k][0]  # calculate gx of pixel

            for k in range(0, 2):
                for l in range(0, 2):
                    pixel_gy += kernel_gy[k][l] * image[j + l][i + k][0]  # calculate gy of pixel

            pixel_result = int(abs(((pixel_gx ** 2) + (pixel_gy ** 2)) ** 0.5))
            resultImage[j][i] = pixel_result

    return resultImage


# Function to apply sobel method
def sobel(image):
    height = image.shape[0]  # takes the number of columns
    width = image.shape[1]  # takes the number of lines

    kernel_gx = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  # Gx
    kernel_gy = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])  # Gy

    resultImage = np.zeros((height, width, 1), np.uint8)

    for i in range(0, width - 1):  # lines
        for j in range(0, height - 1):  # columns
            pixel_gy = 0  # reset gy of pixel
            pixel_gx = 0  # reset gx of pixel

            for k in range(0, 3):
                for l in range(0, 3):
                    pixel_gx += kernel_gx[k][l] * image[j - 1 + k][i - 1 + k][0]  # calculate gx of pixel

            for k in range(0, 3):
                for l in range(0, 3):
                    pixel_gy += kernel_gy[k][l] * image[j - 1 + l][i - 1 + k][0]  # calculate gy of pixel

            pixel_result = int(abs(((pixel_gx ** 2) + (pixel_gy ** 2)) ** 0.5))
            resultImage[j][i] = pixel_result

    return resultImage


# Function to show external limits of the image
def limitExternal(image, kernel):
    dilationImg = dilation(image, kernel)
    erosionImg = erosion(image, kernel)
    return subtraction(dilationImg, erosionImg)  # calculate the subtraction between dilation and erosion


# Function to show internal limits of the image
def limitInternal(image, kernel):
    dilationImg = dilation(image, kernel)
    erosionImg = erosion(image, kernel)
    return subtraction(erosionImg, dilationImg)  # calculate the subtraction between erosion and dilation
