#validate contour
import numpy as np
import cv2

def validate(cnt):    
 rect=cv2.minAreaRect(cnt)  
 box=cv2.cv.BoxPoints(rect) 
 box=np.int0(box)  

 output=False
 h=rect[1][0]
 w=rect[1][1]

 if h>0:
  if ( (w/float(h))>1.6 and (w/float(h))<2.7 ):#( (w/float(h))>1.2 and (w/float(h))<2.2 ) or ( (w/float(h))>2.6 and (w/float(h))<4.4 ) or ( (w/float(h))>1.6 and (w/float(h))<2.7 ):
   output=True 

  #if( (w/float(h))>2.5 and (w/float(h))<4.5 ):
  #if( (w/float(h))>1.5 and (w/float(h))<2.8 ):

 return output

