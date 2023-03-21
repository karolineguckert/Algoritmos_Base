import cv2 as cv2
from skimage import io
import numpy as np

def adicao(image1, p1, image2, p2):
    newImage = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)
    dst = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)
    for i in range(0, image1.shape[0]): #height

        for j in range(0, image1.shape[1]): #width
            #print(image1[i, j] * p1 + image2[i, j] * p2)
            newImage[i, j] = image1[i, j] * p1 + image2[i, j] * p2
            dst = cv2.addWeighted(image1, p1, image2, p2, 0.0)

    #cv2.imshow('meu', newImage)
    #cv2.imshow('addWeigthed', dst)
    cv2.imshow('soma', cv2.hconcat([newImage, dst]))
    cv2.waitKey(0)


image1 = io.imread('images/barco.jpg')
image2 = io.imread('images/flor.jpg')
adicao(image1, 0.5, image2, 0.5)
