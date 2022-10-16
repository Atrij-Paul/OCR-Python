import pytesseract
import cv2
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


img = cv2.imread("C:\\Users\\HP\\Desktop\\Test_0.jpg" , 1)
plt.imshow(img)
plt.show()
img2char = pytesseract.image_to_string(img)
print(img2char)
imgbox = pytesseract.image_to_boxes(img)
print(imgbox)


img_H , img_W , _ = img.shape

for boxes in imgbox.splitlines():
    boxes = boxes.split(' ')
    x , y , w , h = int(boxes[1]) , int(boxes[2]) , int(boxes[3]) , int(boxes[4])
    cv2.rectangle(img , (x , img_H - y) , (w , img_H - h) , ( 0 , 0 , 255) , 3)

plt.imshow(img)
plt.show()