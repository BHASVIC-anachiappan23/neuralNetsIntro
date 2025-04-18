import cv2
import numpy as np

img = cv2.imread("C://Users//User//neuralNetsIntro//fig//zeroTest.png") #since the image is grayscale, we need only one channel and the value '0' indicates just that
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
arr = []
for i in range(gray_image.shape[1]):
    for j in range(gray_image.shape[0]):
        arr.append([(255-gray_image[j][i])/255])
npArrZero = np.array(arr)
img = cv2.imread("C://Users//User//neuralNetsIntro//fig//oneTest.bmp") #since the image is grayscale, we need only one channel and the value '0' indicates just that
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
arr = []
for i in range(gray_image.shape[1]):
    for j in range(gray_image.shape[0]):
        arr.append([(255-gray_image[j][i])/255])
npArrOne = np.array(arr)
