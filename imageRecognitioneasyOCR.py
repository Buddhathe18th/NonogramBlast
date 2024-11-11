import cv2
import numpy as np
import pytesseract

from PIL import Image
from easyocr import Reader
reader = Reader(['en'], gpu=False)


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # your path may be different

# cv2.imshow("Image", image[11:73,100:120])
# print(pytesseract.image_to_string(image[11:73,100:120],config='--psm 6'))

image = Image.open('test1.png')
width,height=image.size
image=image.resize((5*width,5*height)).convert('RGB')
image=np.array(image)
image=image[:, :, ::-1].copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
ret, thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
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

vert=True

topX=66
topY=782
gridSize=124.4

leftX=3898
leftY=3362

i=0
j=14
#vertical
if vert:
    img= thresh[round(topY + gridSize * j+gridSize*0.04):round(topY + gridSize * j + gridSize-gridSize*0.04), round(topX + gridSize * i+gridSize*0.04):round(topX + gridSize * i + gridSize-gridSize*0.04)]
    # img=cropImage(img)
    cv2.imshow("1",img)


    d = reader.readtext(img, allowlist ='0123456789')
    if d != []:
        d = d[0][1]


else:
    img = thresh[round(leftY + gridSize * i+gridSize*0.04):round(leftY + gridSize * i + gridSize-gridSize*0.04),round(leftX + gridSize * j+gridSize*0.04):round(leftX + gridSize * j + gridSize-gridSize*0.04)]
    img = cropImage(img)
    cv2.imshow("1",img)
    d = reader.readtext(img, allowlist ='0123456789')[0][1]

print(d)
cv2.waitKey(0)
cv2.destroyAllWindows()