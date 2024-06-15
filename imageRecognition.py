import cv2
import numpy as np
import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # your path may be different

image  = cv2.imread("tast.png")
# cv2.imshow("Image", image[11:73,100:120])
# print(pytesseract.image_to_string(image[11:73,100:120],config='--psm 6'))

image = Image.open('tast.png')
width,height=image.size
image=image.resize((2*width,2*height)).convert('RGB')
image=np.array(image)
image=image[:, :, ::-1].copy()

vert=True

topX=151
topY=21
gridSize=41.1

leftX=27
leftY=181

i=0
j=1

i=5
j=1
#vertical
if vert:
    img= image[round(topY + gridSize * j):round(topY + gridSize * j + gridSize), round(topX + gridSize * i):round(topX + gridSize * i + gridSize)]
    cv2.imshow("1",img)
    d = pytesseract.image_to_string(img,config='--psm 7 -c tessedit_char_whitelist=23456789')
else:
    img = image[round(leftY + gridSize * i) + 4:round(leftY + gridSize * i + gridSize) - 4,round(leftX + gridSize * j) + 4:round(leftX + gridSize * j + gridSize) - 4]
    cv2.imshow("1",img)
    d = pytesseract.image_to_string(img, config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789')

print(d)

cv2.waitKey(0)
cv2.destroyAllWindows()