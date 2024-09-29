# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:44:13 2021

@author: Jesus-Mtz
"""

import cv2 ## importamos la libreria de opencv
import numpy as np ##importamos numpy como np



img = cv2.imread('coins.png') ##leemos la imagen de entrada y la convertimos a escala de grises
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) 


bordes = cv2.Canny(closing,135,255) ## aplicamos el filtro canny para la detección de bordes seleccionamos un umbral minimo de 135 y un maximo de 255

contours, jerarquía = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours (img2, contours, -1, (0,255,0), 3)

cantidad = len(contours)

img2 = cv2.putText(img2, 'Son '+str(cantidad)+" monedas", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

print('Son '+str(cantidad)+" monedas")

cv2.imshow("original", img)  

cv2.imshow("closing", closing) 

cv2.imshow("canny", bordes)  

cv2.imshow("Result", img2)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()




#Contornos:
    
img = cv2.imread('coins.png') ##leemos la imagen de entrada y la convertimos a escala de grises
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) ##aplicamos la función de cierre a la imagen binarizada, esto funciona 
## aplicando primero una dilatación y posteriormente una erosión

contours, jerarquía = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours (img2, contours, -1, (0,255,0), 3)

cantidad = len(contours)

img2 = cv2.putText(img2, 'Son '+str(cantidad)+" monedas", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

print('Son '+str(cantidad)+" monedas")

cv2.imshow("original", img)  
cv2.imshow("bordes", closing) 
cv2.imshow("Result", img2)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()


##Aplicando lo mismo pero con una imagen en fondo blanco y objetos sobre iluminados


img = cv2.imread('tornillos.jpg') ##leemos la imagen de entrada y la convertimos a escala de grises
img2 = img.copy() ##generamos una copia de la imagen original
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ##convertimos la imagen a escala de grises

_, th = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV) ##binarizamos a la inversa la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 15, 15), np.uint8 )  ## construimos un kernel de 15x15 de solo unos

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) ##aplicamos la función de cierre a la imagen binarizada, esto funciona 
## aplicando primero una dilatación y posteriormente una erosión

""" obtenemos los contornos de la imagen con el metodo de recuperación RETR_TREE y con el metodo de aproximación SIMPLE, 
ademas nos arroja su jerarquia """
contours, jerarquía = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

"""Dibujamos los contornos en la imagen copia de la original, con -1 definimos que dibujaremos todos los contornos
ademas los dibujamos en color verde y con un grosor de linea de 10px"""
cv2.drawContours (img2, contours, -1, (0,255,0), 10)

cantidad = len(contours) ##Obtenemos la cantidad de contornos en la imagen

"""Colocamos texto en la imagen copia, este texto mostrará la cantidad de tornillos, el texto estará posicionado en
el pixel 10,50, tendra una escala de 2 y color rojo, ademas de un grosor de linea de 10px"""
img2 = cv2.putText(img2, 'Son '+str(cantidad)+" tornillos", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 10, cv2.LINE_AA)

print('Son '+str(cantidad)+" tornillos") ## imprimimos en la consola la cantidad de tornillos
cv2.namedWindow("original",cv2.WINDOW_NORMAL)
cv2.namedWindow("bordes",cv2.WINDOW_NORMAL)
cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
cv2.imshow("original", img)  
cv2.imshow("bordes", closing) 
cv2.imshow("Result", img2)  

cv2.waitKey(0)  
cv2.destroyAllWindows()