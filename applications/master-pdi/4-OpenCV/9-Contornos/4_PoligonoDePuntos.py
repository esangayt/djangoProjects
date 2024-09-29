# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:25:47 2021

@author: Jesus-Mtz
"""

import cv2
import numpy as np

img = cv2.imread('contorno2.jpeg') ##leemos la imagen de entrada y la convertimos a escala de grises
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) ##aplicamos la función de cierre a la imagen binarizada, esto funciona 
## aplicando primero una dilatación y posteriormente una erosión

contours, jerarquía = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contornosLista = [] ##creamos una lista vacia donde guardaremos los contornos
for index in range(len(contours)):
    
    area = cv2.contourArea(contours[index])
    
    if area > 50000: ## condicionamos los contornos a dibujar, solo se dibujarán y procesaran los contornos con area mayor a 50000 px
        contornosLista.append(contours[index]) ## agregamos los contornos mayores a 50000 px en la lista
        
        cnt = contours[index]
        M = cv2.moments(cnt)
            
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        
        # img2 = cv2.putText(img2, str(area)+"px", (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 1, cv2.LINE_AA)
        
        # cx = cx +500 ##fuera del contorno
        # cx = cx +444 ## en el borde
        
        # cx,cy = tuple(cnt [cnt[:,:, 1].argmin()][0]) ## mas arriba
        # cx,cy = tuple(cnt[cnt[:,:,1].argmax()][0]) ## mas abajo
        # cx,cy = tuple(cnt[cnt[:,:,0].argmin()][0]) ## mas a la izquierda
        # cx,cy = tuple(cnt[cnt[:,:,0].argmax()][0]) ## mas a la derecha
        
        res = cv2.pointPolygonTest (cnt, (int(cx),int(cy)), False ) ##Evaluamos si un punto se encuentra dentro, fuera o en el borde de un contorno
        
        if res == 1:
            img2 = cv2.circle(img2, (cx,cy), radius=10, color=(0, 255, 0), thickness=-1)
            img2 = cv2.putText(img2, 'El punto se encuentra dentro del contorno', (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
        elif res == -1:
            img2 = cv2.circle(img2, (cx,cy), radius=10, color=(0, 0, 255), thickness=-1)
            img2 = cv2.putText(img2, 'El punto se encuentra fuera del contorno', (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA) 
        elif res == 0:
            img2 = cv2.circle(img2, (cx,cy), radius=10, color=(255, 0, 0), thickness=-1)
            img2 = cv2.putText(img2, 'El punto se encuentra en el borde del contorno', (10,50), cv2.FONT_HERSHEY_SIMPLEX, 
                               1, (255,0,0), 2, cv2.LINE_AA)
    
    cv2.drawContours (img2, contornosLista, -1, (0,255,0), 5) ## dibujamos los contornos

cantidad = len(contornosLista)


print('Son '+str(cantidad)+" monedas")
cv2.namedWindow("original",cv2.WINDOW_NORMAL)
cv2.namedWindow("bordes",cv2.WINDOW_NORMAL)
cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
cv2.imshow("original", img)  
cv2.imshow("bordes", closing) 
cv2.imshow("Result", img2)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()