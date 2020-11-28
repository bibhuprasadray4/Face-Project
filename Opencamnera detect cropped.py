# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:52:03 2020

@author: cttc
"""

import cv2
import numpy as np
import urllib

URL = "http://10.32.63.141:8080/shot.jpg"

cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")




while True:
  imgresp = urllib.request.urlopen(URL)
  imgarray = np.array(bytearray(imgresp.read()),
                      dtype = np.uint8)
  frame = cv2.imdecode(imgarray, -1)
  
  frame = cv2.resize(frame,(680,420))
  
  
                                
  faces = cascade.detectMultiScale(frame)
  
  for x,y,w,h in faces:
    cv2.rectangle(frame,(x,y),(x+w,y+h),
                  (0,0,255),2)
    #For cropping face
    face_image = frame[y:y+h,x:x+h]
    
    face_image = cv2.resize(face_image,(224,224))
    
    cv2.imshow('face',face_image)
    
  cv2.imshow('video',frame)
  
  if cv2.waitKey(1) == 27:
    break

cv2.destroyAllWindows()


  