# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:59:07 2021

@author: Jesus-Mtz
"""

import cv2

cap = cv2.VideoCapture(1) 

f = 0 

while True: 
    
  ret, frame = cap.read() 
  
  gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
  
  if f == 10: 
    fondo = gris 
    
  if f > 10:
    dif = cv2.absdiff(gris, fondo)
    
    _, th = cv2.threshold(dif, 15, 255, cv2.THRESH_BINARY) 
    
    contornos, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    
    for c in contornos: 
        
      area = cv2.contourArea(c) 
      
      if area > 200: 
        x,y,w,h = cv2.boundingRect(c) 
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)  
        
  cv2.imshow('Frame',frame) 
  
  f = f+1 

  
  if cv2.waitKey(1) & 0xFF == ord ('q'):
    break

cap.release()
cv2.destroyAllWindows()