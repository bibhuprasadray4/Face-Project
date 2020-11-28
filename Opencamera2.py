# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:39:01 2020

@author: cttc
"""

import cv2
import urllib

URL = "http://10.32.63.141:8080/shot.jpg"


cap = cv2.VideoCapture(0)

ret,frame = cap.read()

while ret:
  ret,frame = cap.read()
  cv2.imshow('video',frame)
  
  if cv2.waitKey(1) == 27:
    break
cap.release()
cv2.destroyAllWindows()
  


  
  
