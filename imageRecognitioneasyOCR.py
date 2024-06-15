import cv2
import numpy as np
import pytesseract

from PIL import Image
from easyocr import Reader
reader = Reader(['en'], gpu=False)


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # your path may be different

image  = cv2.imread("tast.png")
# cv2.imshow("Image", image[11:73,100:120])
# print(pytesseract.image_to_string(image[11:73,100:120],config='--psm 6'))

image = Image.open('tast.png')
width,height=image.size
image=image.resize((5*width,5*height)).convert('RGB')
image=np.array(image)
image=image[:, :, ::-1].copy()

vert=True

topX=377
topY=55
gridSize=102.8

leftX=69
leftY=452

i=1
j=3
#vertical
if vert:
    img= image[round(topY + gridSize * j+gridSize*0.04):round(topY + gridSize * j + gridSize-gridSize*0.04), round(topX + gridSize * i+gridSize*0.04):round(topX + gridSize * i + gridSize-gridSize*0.04)]
    cv2.imshow("1",img)
    d = reader.readtext(img, allowlist ='0123456789')[0][1]
else:
    img = image[round(leftY + gridSize * i+gridSize*0.04):round(leftY + gridSize * i + gridSize-gridSize*0.04),round(leftX + gridSize * j+gridSize*0.04):round(leftX + gridSize * j + gridSize-gridSize*0.04)]
    cv2.imshow("1",img)
    d = reader.readtext(img, allowlist ='0123456789')[0][1]

print(d)

cv2.waitKey(0)
cv2.destroyAllWindows()