import numpy as np
import cv2
import matplotlib.pyplot as plt
import filter

#Read image
img = cv2.imread('/home/jera/chapa2.jpg')

# convert into grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# blur the image
blur=cv2.GaussianBlur(gray,(5,5),0)
#cv2.imshow("blur",blur)

# find the sobel gradient. use the kernel size to be 3
sobelx=cv2.Sobel(blur, cv2.CV_8U, 1, 0, ksize=3)
cv2.imshow("sobelx",sobelx)


#Otsu thresholding
ret, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

h,w=thresh.shape

horizontalsize=w/30


contours, hier = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
 rect=cv2.minAreaRect(cnt)  
 box=cv2.cv.BoxPoints(rect) 
 box=np.int0(box)  
 cv2.drawContours(img, [box], 0, (0,0,255),2)

cv2.imshow("edged",img)
cv2.waitKey(0)


