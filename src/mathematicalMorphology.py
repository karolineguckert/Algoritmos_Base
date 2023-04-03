import numpy as np


def erosion(image, kernel):
    rows = image.shape[0]
    cols = image.shape[1]

    resultImage = np.zeros([rows, cols, 4], np.uint8)

    start = int(len(kernel) / 2)
    row_element = len(kernel)
    col_element = len(kernel[0])

    for i in range(start, cols - start):  # lines
        for j in range(start, rows - start):  # columns
            pixelImage = image[j][i]

            countKernel = 0
            countAll = 0

            for k in range(0, row_element):  # lines
                for l in range(0, col_element):  # columns
                    pixelKernel = kernel[k][l]

                    # contabiliza quantos valores no kernel são:
                    # não nulos
                    if pixelKernel != 0:
                        countKernel += 1

                        # contabiliza valores não nulos coincidentes
                        # imagem e kernel
                        positionLine = i - start + k
                        positionColumn = j - start + l

                        if image[positionColumn][positionLine][0] != 0:
                            countAll += 1

            if countKernel == countAll:
                resultImage[j][i] = pixelImage

    return resultImage


def dilation(image, kernel):
    rows = image.shape[0]
    cols = image.shape[1]

    resultImage = np.zeros([rows, cols, 4], np.uint8)

    start = int(len(kernel) / 2)
    row_element = len(kernel)
    col_element = len(kernel[0])

    for i in range(start, cols - start):  # columns
        for j in range(start, rows - start):  # lines
            pixelImage = image[j][i]

            if pixelImage[0] != 0:
                for k in range(0, row_element):  # lines
                    for l in range(0, col_element):  # columns
                        pixelKernel = kernel[k][l]

                        if pixelKernel == 1:
                            resultImage[j - start + l][i - start + k] = pixelImage

    return resultImage


def opening(image, kernel):
    imageErosion = erosion(image, kernel)
    return dilation(imageErosion, kernel)


def closing(image, kernel):
    imageDilation = dilation(image, kernel)
    return erosion(imageDilation, kernel)