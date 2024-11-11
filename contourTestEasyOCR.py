import cv2
import numpy as np
import pytesseract
from PIL import Image

from easyocr import Reader
reader = Reader(['en'])

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # your path may be different


size=10

image = Image.open('test1.png')
width,height=image.size
image=image.resize((5*width,5*height)).convert('RGB')
image=np.array(image)
image=image[:, :, ::-1].copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
ret, thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def cropImage(img):
    # Crop left pixels
    leftSum=img[int(gridSize/2), 0]

    while leftSum<200:
        h, w = img.shape[:2]
        img=img[0:h,round(w*0.01):w-1]


        leftSum=img[int(gridSize/2), 0]

    h, w = img.shape[:2]
    # Crop right side
    rightSum = img[int(gridSize / 2), w-1]


    while rightSum < 200:
        h, w = img.shape[:2]
        img = img[0:h, 0:round(w * 0.99)]
        h, w = img.shape[:2]

        rightSum = img[int(gridSize / 2), w-1]

    return img

max_area = 0
c = 0
for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
                if area > max_area:
                    max_area = area
                    best_cnt = i
                    # image = cv2.drawContours(image, contours, c, (0, 255, 0), 3)
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

xySum=[]
for i in approx:
    xySum.append(i[0][0]+i[0][1])
xySumCopy=xySum.copy()

point1=approx[xySum.index(min(xySum))]
xySum.pop(xySum.index(min(xySum)))
point2=approx[xySumCopy.index(min(xySum))]
xySum.pop(xySum.index(min(xySum)))
topLeftOfSquare=approx[xySumCopy.index(min(xySum))]
bottomRight=approx[xySumCopy.index(max(xySum))]

if point1[0][0]<point2[0][0]:
    top=point1
    side=point2
else:
    top = point2
    side = point1






gridSize=-1*((top[0][1]-bottomRight[0][1])+(side[0][0]-bottomRight[0][0]))/(2*size)
topSize=round(pow((top[0][0]-topLeftOfSquare[0][0])**2+(top[0][1]-topLeftOfSquare[0][1])**2,0.5)/gridSize)
sideSize=round(pow((side[0][0]-side[0][0])**2+(side[0][1]-side[0][1])**2,0.5)/gridSize)



topX=top[0][0]
topY=top[0][1]

leftX=side[0][0]
leftY=side[0][1]

print(topSize)


print(topX)
print(topY)

print(gridSize)

print(leftX)
print(leftY)
print(approx)

def topNumbers():
    nums = []
    for i in range(size):
        k = []
        for j in range(topSize):

            img= thresh[round(topY + gridSize * j+gridSize*0.04):round(topY + gridSize * j + gridSize-gridSize*0.04), round(topX + gridSize * i+gridSize*0.04):round(topX + gridSize * i + gridSize-gridSize*0.04)]
            print(i)
            print(j)
            img=cropImage(img)
            d = reader.readtext(img, allowlist ='0123456789')

            if d==[]:
                continue
            k.append(d[0][1])
        nums.append(k)
    return nums


def sideNumbers():
    nums = []
    for i in range(size):
        k = []
        for j in range(sideSize):
            img = thresh[round(leftY + gridSize * i+gridSize*0.04):round(leftY + gridSize * i + gridSize-gridSize*0.04),round(leftX + gridSize * j+gridSize*0.04):round(leftX + gridSize * j + gridSize-gridSize*0.04)]
            img = cropImage(img)
            d = reader.readtext(img, allowlist ='0123456789')

            if d == []:
                continue
            k.append(d[0][1])
        nums.append(k)
    return nums

nums=topNumbers()+sideNumbers()
print(nums)


cv2.imshow("Final Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
