# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:17:00 2020

@author: bibhu
"""


import sqlite3 as sql
from numpy import asarray
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
import io
import urllib
import cv2
import numpy as np
from datetime import date
from scipy.spatial.distance import cosine
model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
face_data = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(face_data)


def adapt_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sql.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)

sql.register_adapter(np.ndarray, adapt_array)
sql.register_converter("array", convert_array)

def preprocess(img):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = img.reshape(1,224,224,3)
        img = asarray(img,np.float32)
        img = preprocess_input(img,version=2)
        return img
    
URL =  "http://25.163.251.138:8080/shot.jpg"
cur = sql.connect('attendence_sys.db',detect_types=sql.PARSE_DECLTYPES)
query = """SELECT * FROM student_face_data"""
rate = cur.execute(query)
rate = rate.fetchall()
cur.close()


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
    newemb = model.predict(preprocess(face_image))
    for i in rate:
        if cosine (newemb,i[1])<0.2:
            print('done')
            cur = sql.connect('attendence_sys.db',detect_types=sql.PARSE_DECLTYPES)
            query = """INSERT INTO student_attendence(Sid,date,attendence) VALUES(?,?,?)"""
            cur.execute(query,(i[0],date.today().strftime("%d-%m-%y")
                               ,"P"))
            
            cur.close()
             
    
                
  cv2.imshow('video',frame)
  
  if cv2.waitKey(1) == 27:
    break

cv2.destroyAllWindows()


  
