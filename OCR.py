'''Any image whenevr scanned is made into a bitmap'''
'''A Bitmap is just a matrix of black and white dots(image is first converted to grayscale)'''
'''Then after that the contrast and brightness will be managed'''

import pytesseract
import cv2
import numpy as np


def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def get_grayscale(img):
    return cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    return cv2.medianBlur(img , 5)

def thresholding(img):
    return cv2.threshold(img , 0 , 255 , cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]



img = cv2.imread("C:\\Users\\HP\\Downloads\\surf.jpg")

img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))