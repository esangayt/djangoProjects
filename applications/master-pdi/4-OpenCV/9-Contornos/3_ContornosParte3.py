# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:36:30 2021

@author: Jesus-Mtz
"""

import numpy as np
import cv2

##Geometria delimitadora 

img = cv2.imread('contorno2.jpeg') ##leemos la imagen de entrada y la convertimos a escala de grises
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) ##aplicamos la función de cierre a la imagen binarizada, esto funciona 
## aplicando primero una dilatación y posteriormente una erosión

contours, jerarquía = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contornosLista = []
for index in range(len(contours)):
    
    area = cv2.contourArea(contours[index])

    if area > 50000:
        cnt = contours[index]
        M = cv2.moments(cnt) ## calculamos el momento del contorno
        
        rect = cv2.minAreaRect(cnt) ## calculamos el ractangulo minimo delimitador del contorno
        box = cv2.boxPoints(rect) ##obtenemos los puntos del rectangulo
        box = np.int0(box) ##convertimos los puntos float a enteros
        contornosLista.append(box) ##guardamos el contorno en nuestra lista de contornos
        
        (x, y),radio = cv2.minEnclosingCircle(cnt) ## encontrar el circulo minimo que se ajusta al contorno
        centro = (int(x), int(y)) 
        radio = int(radio)
        cv2.circle (img2, centro, radio, (0,0,255), 2) ##dibujamos el circulo minimo
        elipse = cv2.fitEllipse(cnt)
        cv2.ellipse(img2, elipse, (255,0,0), 2)
        
        ## calculamos el centroide del contorno
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        img2 = cv2.circle(img2, (cx,cy), radius=5, color=(0, 0, 255), thickness=-1)
        img2 = cv2.putText(img2, str(area)+"px", (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 1, cv2.LINE_AA)

    cv2.drawContours (img2, contornosLista, -1, (0,255,0), 5) ## dibujamos los contornos de la lista
cantidad = len(contornosLista)



img2 = cv2.putText(img2, 'Son '+str(cantidad)+" contornos", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

print('Son '+str(cantidad)+" monedas")
cv2.namedWindow("original",cv2.WINDOW_NORMAL)
cv2.namedWindow("bordes",cv2.WINDOW_NORMAL)
cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
cv2.imshow("original", img)  
cv2.imshow("bordes", closing) 
cv2.imshow("Result", img2)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()