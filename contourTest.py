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
print(topSize)

topLeftX=approx[0][0][0]
topLeftY=approx[0][0][1]

nums=[]
for i in range(size):
    print(i)
    k = []
    for j in range(topSize):

        img=image[round(topLeftY+gridSize*j)+2:round(topLeftY+gridSize*j+gridSize)-2,round(topLeftX+gridSize*i)+2:round(topLeftX+gridSize*i+gridSize)-2]

        d = pytesseract.image_to_string(img,config='--psm 6')

        k.append(d)
        print(k)
    nums.append(k)

print(nums)

mask = np.zeros((gray.shape),np.uint8)
cv2.drawContours(mask,[best_cnt],0,255,-1)
cv2.drawContours(mask,[best_cnt],0,0,2)

out = np.zeros_like(gray)
out[mask == 255] = gray[mask == 255]


blur = cv2.GaussianBlur(out, (5,5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
cv2.imshow("thresh1", thresh)


cv2.imshow("Final Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
