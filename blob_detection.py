import numpy as np
import cv2
from autoCanny import *


def is_plate(roi_gray):
 out=False

 H,W=roi_gray.shape
 if H>0 and W>0:
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
  cl1 = clahe.apply(roi_gray)
 

  # blur the image
  blur=cv2.GaussianBlur(roi_gray,(5,5),0)


  # blur the image
  
  blur=cv2.bilateralFilter(roi_gray,3,45,45)
  
  #cv2.imshow('blur',blur)
  #cv2.waitKey(0)

  #Otsu thresholding
  ret, thresh = cv2.threshold(blur.copy(),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  #cv2.imshow('tresh',thresh)
  #cv2.waitKey(0)

  '''#Morphological Closing

  h,w=thresh.shape
  v_size=h/30

  se=cv2.getStructuringElement(cv2.MORPH_RECT,(1,v_size))
  closing=cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, se)'''


  #Morphological opening diamond
  diamond=np.uint8([[0, 0, 1, 0, 0],
                   [0, 1, 1, 1, 0],
                   [1, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0],
                   [0, 0, 1, 0, 0]])

  img_open=cv2.morphologyEx(thresh, cv2.MORPH_OPEN, diamond)
  
  #cv2.imshow('open',img_open)
  #cv2.waitKey(0)



  #find contours
  contours, hier = cv2.findContours(img_open, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


  mask = np.ones(blur.shape[:2], dtype="uint8") 
  i=0

  for cnt in contours:
   x,y,w,h = cv2.boundingRect(cnt)
    
   if h>0:
   # print ("h=",h,"w=",w,"rt=",w/float(h))
    if h/float(w)>1 and h/float(w)<7:
     #print ("h=",h,"w=",w,"rt=",h/float(w))
     #cv2.rectangle(blur,(x,y),(x+w,y+h),(0,255,0),2)
     cv2.drawContours(mask, [cnt], 0, 255, -1)
     i+=1
  '''
  #Morphological dilate characters areas
  mask = cv2.bitwise_not(mask)
  kernel = np.ones((5,5),np.uint8)
  mask = cv2.erode(mask,kernel,iterations = 1)
  cv2.imshow('',mask)
  cv2.waitKey(0)
  '''
 #edges=auto_canny(img_open)
 #Substract characters edges
 #edges = cv2.bitwise_and(edges, mask)

 #cv2.imshow('blur_char',blur)
 #cv2.waitKey(0)

 #cv2.imshow('mask',edges)
 #cv2.waitKey(0)
   
  if i>0:
   #Morphological dilate characters areas
   mask = cv2.bitwise_not(mask)
   kernel = np.ones((5,5),np.uint8)
   mask = cv2.erode(mask,kernel,iterations = 1)
   #cv2.imshow('',mask)
   #cv2.waitKey(0)

   out=True
  #print "finish blob"
  return out,blur,img_open,mask
 else:
  #print "finish blob"
  return out,None,None,None





