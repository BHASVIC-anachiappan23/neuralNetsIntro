import cv2
import numpy as np
#You can draw numbers on a file and input it and this will give you a np array which you can do the feedforward on a network
def giveArr(filePath):
    img = cv2.imread(filePath) #since the image is grayscale, we need only one channel and the value '0' indicates just that
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    arr = []
    for i in range(gray_image.shape[1]):
        for j in range(gray_image.shape[0]):
            arr.append([np.float32((255-gray_image[i][j])/255)])
    return np.array(arr)
