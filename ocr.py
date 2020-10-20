import os
import tesseract
import cv2.cv as cv
import numpy as np
import locale

def read():
 i=0
 string=''
 percents=[]
 path="/home/jera/segmentos/"
 dirs = os.listdir(path)
 dirs.sort()

 ### tesseract OCR api setup
 locale.setlocale(locale.LC_NUMERIC,"C")
 #locale.setlocale(locale.LC_ALL, "C")
 api = tesseract.TessBaseAPI()
 api.Init("/usr/share/tesseract-ocr","lus",tesseract.OEM_DEFAULT)
 api.SetVariable("tessedit_char_whitelist", "ABCDEFGHJKLMNOPRQSTUVWXYZ")
 api.SetPageSegMode(tesseract.PSM_SINGLE_CHAR)

 #walk through dir 
 #walk through dir 
 for x in dirs:
  # path to individual file
  x=path+x

  #open image
  image=cv.LoadImage((x), cv.CV_LOAD_IMAGE_GRAYSCALE)
  tesseract.SetCvImage(image,api)
  text=api.GetUTF8Text()
  conf=api.MeanTextConf()
  image=None
  if (conf)>76 :
   print text[0]
   string+=text[0]
   percents.append(conf)
   i+=1
   if i==3:
    api.SetVariable("tessedit_char_whitelist", "0123456789")
   if i>=6: 
    #os.remove(x)
    break
  #os.remove(x)



 perc=sorted(percents)
 #Release memory
 api.End()
  
 if len(string)==6:
  print string,perc[0]
 else:
  print "Error"

read()



