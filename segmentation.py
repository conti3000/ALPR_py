import numpy as np
import cv2
import matplotlib.pyplot as plt
#from scipy import signal
from detect_peaks import detect_peaks
#import matplotlib.pyplot as plt
import uuid

def cut(blur):
 lines=None
 # find the sobel gradient. use the kernel size to be 3
 #sobelx=cv2.Sobel(blur, cv2.CV_8U, 1, 0, ksize=3)

 h,w=blur.shape[:2]
 blur=blur[0+int(h*0.3): h , 0: w]
 copy=cv2.cvtColor(blur, cv2.COLOR_GRAY2RGB)


 #Otsu thresholding
 ret, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

 #cv2.imshow('th',thresh)
 #cv2.imwrite('str(uuid.uuid1()).jpg',thresh)
 #cv2.waitKey(0)
 
 ##################
 ###########
 ########
 #find contours
 copy_vert=thresh.copy()
 #cv2.imshow('d',copy_vert)
   
 contours, hier = cv2.findContours(copy_vert.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
 for cnt in contours:
  x,y,w,h = cv2.boundingRect(cnt)
  if h>0:
   if (h/float(w)>2 and h/float(w)<3) or (h/float(w)>4.5 and h/float(w)<5.5):
    cv2.rectangle(copy_vert,(x,y),(x+w,y+h),(0,255,0),cv2.cv.CV_FILLED)

 #cv2.imshow('d',copy_vert)
 #cv2.waitKey(0)
 ########
 ############
 #################
 ######################
 
 #vertical histogram
 vert_hist=np.sum(copy_vert==255, axis=1)
 h,w1=thresh.shape

 #finding peaks indexes in vertical histogram projection


 data=vert_hist
 peakindy=detect_peaks(data,mpd=int(0.2*h), show=False)
 #print peakindy
 #peakindy= signal.find_peaks_cwt(data,np.arange(1,int(0.2*h)))

 #finding peaks average in vertical histogram projection
 cnt=0
 peakvaluesy=[]
 for j in peakindy:
  peakvaluesy.append(data[j])
  cnt+=1
 if cnt>=2:
  maxy=int(max(peakvaluesy))

  #filtering peaks in vertical histogram projection that are above average
  filteredy=[]
  for j in peakindy:
   if data[j]>= 0.9*maxy:
    cv2.line(copy,(0,j),(w1,j),(255,0,0),2)
    filteredy.append(j)

  if len(filteredy)>=2:
   #Crop image in vertical region of the charaters

   y1=filteredy[0]
   y2=filteredy[1]

   roi_vert=thresh[y1: y2, 0: w1]
   
   #finding horizonral histogram projection
   horz_hist=np.sum(roi_vert==255, axis=0)
 
   #finding peaks indexes in horizontal histogram projection
   peakindx= detect_peaks(horz_hist,show=False)


   maximum=int(max(horz_hist)*0.95)

   #findig average of peaks in horizontal histogram
   '''
   cnt=0
   avg=0
   for i in peakindx:
    avg+=horz_hist[i]
    cnt+=1
   if cnt>0:
    avg=avg/cnt
   '''
   #Draw a line for peaks above average in horizontal projection and crop segment characters
   i0=0
   j=0
   
   #copy=blur.copy
   for i in peakindx:
    if horz_hist[i]>maximum:
     cv2.line(copy,(i,0),(i,h),(255,255,0),1)
     roi_vert=thresh[y1: y2, i0: i]
    
     #roi_vert=cv2.resize(roi_vert,(50, 200))
     #roi_vert= cv2.equalizeHist(roi_vert)

     #big=np.zeros((300,100),np.uint8)
     #big=cv2.bitwise_not(big)

     #small=roi_vert
     #x_offset=y_offset=25
     #y_offset=50
     #big[y_offset:y_offset+small.shape[0], x_offset:x_offset+small.shape[1]] = small
     #kernel = np.ones((5,5),np.uint8)
     #roi_vert = cv2.erode(big,kernel,iterations = 1)
    
     path='/root/up/segmentos/segment'+str(j)+'.jpg'
     cv2.imwrite(path,roi_vert)
     j+=1
     i0=i
     
   lines=copy
   #cv2.imshow('lines',lines)
   return lines


   #cv2.imshow('lines',copy)
   #cv2.imwrite('str(uuid.uuid1()).jpg',lines)
   #cv2.waitKey(0)

     
















