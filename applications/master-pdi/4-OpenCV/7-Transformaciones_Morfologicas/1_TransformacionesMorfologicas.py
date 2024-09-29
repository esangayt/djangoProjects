# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:52:34 2021

@author: Jesus-Mtz
"""

import cv2 ## importamos la libreria de opencv
import numpy as np ##importamos numpy como np

img = cv2.imread("coins.png",0) ## leemos la imagen coins.png en escala de grises y la guardamos en img

_, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

dilation = cv2.dilate(th,kernel,iterations = 1) ## aplicamos una dilatación a la imagen con una sola iteración

erosion = cv2.erode(th,kernel,iterations = 2) ## aplicamos una erosión de 2 iteraciones a la imagen dilatada 

cv2.namedWindow("original",cv2.WINDOW_NORMAL) 
cv2.namedWindow("binarizada",cv2.WINDOW_NORMAL) 
cv2.namedWindow("erode",cv2.WINDOW_NORMAL) 
cv2.namedWindow("dilate",cv2.WINDOW_NORMAL) 

cv2.imshow("original",img)
cv2.imshow("binarizada", th)
cv2.imshow("erode", erosion)
cv2.imshow("dilate", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()


## Otra forma de realizarlo:

img = cv2.imread("coins.png",0) ## leemos la imagen coins.png en escala de grises y la guardamos en img

_, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) ##aplicamos la función de cierre a la imagen binarizada, esto funciona 
## aplicando primero una dilatación y posteriormente una erosión

cv2.imshow("original",img)
cv2.imshow("binarizada", th)
cv2.imshow("erode", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()


##Eliminar ruido con una erosión seguida de una dilatación

img = cv2.imread("opening.png",0) ## leemos la imagen coins.png en escala de grises y la guardamos en img

_, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

erosion = cv2.erode(th,kernel,iterations = 1) ## aplicamos una erosión de 1 iteraciones a la imagen binarizada 

dilation = cv2.dilate(erosion,kernel,iterations = 1) ## aplicamos una dilatación a la imagen con una sola iteración

cv2.namedWindow("original",cv2.WINDOW_NORMAL) 
cv2.namedWindow("binarizada",cv2.WINDOW_NORMAL) 
cv2.namedWindow("erode",cv2.WINDOW_NORMAL) 
cv2.namedWindow("dilate",cv2.WINDOW_NORMAL) 

cv2.imshow("original",img)
cv2.imshow("binarizada", th)
cv2.imshow("erode", erosion)
cv2.imshow("dilate", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()


##otra forma de realizarlo:
    
img = cv2.imread("opening.png",0) ## leemos la imagen coins.png en escala de grises y la guardamos en img

_, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel) ##aplicamos la función de apertura a la imagen binarizada, esto funciona 
# aplicando primero una erosión y posteriormente una dilatación

cv2.namedWindow("original",cv2.WINDOW_NORMAL) 
cv2.namedWindow("binarizada",cv2.WINDOW_NORMAL) 
cv2.namedWindow("dilate",cv2.WINDOW_NORMAL) 


cv2.imshow("original",img)
cv2.imshow("binarizada", th)

cv2.imshow("dilate", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
