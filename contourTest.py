import cv2
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # your path may be different


size=10

image  = cv2.imread("10.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
ret, thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_area = 0
c = 0
for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
                if area > max_area:
                    max_area = area
                    best_cnt = i
                    image = cv2.drawContours(image, contours, c, (0, 255, 0), 3)
        c+=1
best_cnt=0
c=0
secondMax=0
for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
                if area < max_area and area>secondMax:
                    secondMax = area
                    best_cnt = i
                    image = cv2.drawContours(image, contours, c, (0, 255, 0), 3)
        c+=1


approx = cv2.approxPolyDP(best_cnt, 0.013 * cv2.arcLength(best_cnt, True), True)
print(approx)
gridSize=pow((approx[0][0][0]-approx[1][0][0])**2+(approx[0][0][1]-approx[1][0][1])**2,0.5)/size
print(gridSize)
topSize=round(pow((approx[0][0][0]-approx[5][0][0])**2+(approx[0][0][1]-approx[5][0][1])**2,0.5)/gridSize)
sideSize=round(pow((approx[4][0][0]-approx[5][0][0])**2+(approx[4][0][1]-approx[5][0][1])**2,0.5)/gridSize)
print(sideSize)

topX=approx[0][0][0]
topY=approx[0][0][1]

leftX=approx[4][0][0]
leftY=approx[4][0][1]


def topNumbers():
    nums = []
    for i in range(size):
        k = []
        for j in range(topSize):

            img= image[round(topY + gridSize * j) + 2:round(topY + gridSize * j + gridSize) - 2, round(topX + gridSize * i) + 4:round(topX + gridSize * i + gridSize) - 4]

            d = pytesseract.image_to_string(img,config='--psm 6')

            if d=="":
                continue
            k.append(d[:-1])
            print(k)
        nums.append(k)
    return nums


def sideNumbers():
    nums = []
    for i in range(size):
        k = []
        for j in range(sideSize):
            img = image[round(leftY + gridSize * i) + 2:round(leftY + gridSize * i + gridSize) - 2,round(leftX + gridSize * j) + 4:round(leftX + gridSize * j + gridSize) - 4]

            d = pytesseract.image_to_string(img, config='--psm 6')

            if d == "":
                continue
            k.append(d[:-1])
            print(k)
        nums.append(k)
    return nums

nums=topNumbers()+sideNumbers()



cv2.imshow("Final Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
