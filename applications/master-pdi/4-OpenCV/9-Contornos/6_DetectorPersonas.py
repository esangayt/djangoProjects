# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:38:15 2021

@author: Jesus-Mtz
"""

##Aplicación del test de poligono en aplicación de vigilancia

import cv2
import numpy as np
from datetime import datetime

clasificador = cv2.CascadeClassifier('haarcascade_fullbody.xml')
cap = cv2.VideoCapture('personas.avi')

cuenta = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        if cuenta ==0:
            roi=cv2.selectROI(frame)
            x1 = roi[0]
            y1 = roi[1]
            w1 = roi[2]
            h1 = roi[3]

        if cuenta > 1:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img2=frame.copy()
            personas = clasificador.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=1,
                                                     minSize=(35,35), maxSize=(150,150))
            try:
                for (x,y,w,h) in personas:
                  cx = int((x+(w/2)))
                  cy = int((y+(h/2)))

                  box = np.array([[x1,y1],[x1+w1,y1],[x1+w1,y1+h1],[x1,y1+h1]])
                  box = np.int0(box)
                  contornos = [box]
                  res = cv2.pointPolygonTest (box, (cx,cy), False )
                  cv2.drawContours (frame, contornos, -1, (255,0,0), 5)

                  if res == 1:
                      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                      cropped_image = img2[y:y+h, x:x+w]
                      date = datetime.now()
                      nombreArchivo = "./capturas/"+str(date.hour)+str(date.minute)+str(date.second)+'.jpg'
                      cv2.imwrite(nombreArchivo,cropped_image)

                cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)
                cv2.namedWindow("crop",cv2.WINDOW_NORMAL)
                cv2.imshow('Frame',frame)
                cv2.imshow('crop',cropped_image)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            except:
                pass
        cuenta += 1
    else:
        break

cap.release()
cv2.destroyAllWindows()