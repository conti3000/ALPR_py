import numpy as np
import cv2
import sys

plateCascade = cv2.CascadeClassifier('/root/up1/cascade.xml')

def detect_plate(image):

 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


 # Detect plates in the image
 plates = plateCascade.detectMultiScale(
     gray,
     scaleFactor=1.3,
     minNeighbors=5,
     minSize=(30, 30),
     flags = cv2.cv.CV_HAAR_SCALE_IMAGE
 )


     
 if len(plates)>0:
  for (x, y, w, h) in plates:
   cv2.rectangle(image, (x-int(w*0.20), y-int(h*0.30)), (x+w+int(w*0.15), y+h+int(h*0.15)), (0, 255, 0), 2)   
   image=cv2.resize(image, (600, 450))
   cv2.imshow('rec',image)

   roi_gray=gray[y-int(h*0.15): y+h+int(h*0.075), x-int(w*0.10): x+w+int(w*0.075)]
   
    #print "finish detect"
   return gray,(x,y,w,h),roi_gray
 else:
  return gray,None,None

