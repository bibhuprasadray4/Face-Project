# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:16:16 2020

@author: cttc
"""

import cv2
import numpy as np
import urllib

URL = "http://10.32.63.141:8080/shot.jpg"




while True:
  imgresp = urllib.request.urlopen(URL)
  imgarray = np.array(bytearray(imgresp.read()),
                      dtype = np.uint8)
  frame = cv2.imdecode(imgarray, -1)
                                
  
  cv2.imshow('video',frame)
  
  if cv2.waitKey(1) == 27:
    break
cap.release()
cv2.destroyAllWindows()
  


  