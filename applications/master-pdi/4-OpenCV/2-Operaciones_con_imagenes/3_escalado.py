# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:23:57 2021

@author: Jesus-Mtz
"""

## Metodo 1

import cv2 ##Importar opencv
import numpy as np ##importamos la libreria numpy como np

# imagen = cv2.imread("1.jpg") ##leemos la imagen con la que trabajaremos y la guardamos en la variable imagen
# h,w,c = imagen.shape ## obtenemos las dimensiones de la imagen

# escala = 2 ## definimos el factor de escala 
# tMatrix = np.array([[escala,0,0],[0,escala,0],[0,escala,1]]) ##creamos la martiz de transformación para escalado
# imagen2 = np.zeros((h*escala, w*escala, 3),np.uint8) ##creamos la imagen base sobre la cual escribiremos la imagen escalada

# for i in range(h): ##recorremos la altura de la imagen
#     for j in range(w):  ##recorremos el ancho de la imagen
#         pixel = imagen[i,j] ##obtenemos el píxel que reposicionaremos
#         vector = np.array([j,i,1])  ##formamos nuestro vector
#         result = np.dot(tMatrix,vector) ##realizamos producto punto de la matriz con el vector
#         x = result[0] ##obtenemos el resultado de x del vector resultante del producto punto
#         y = result[1] ##obtenemos el resultado de y del vector resultante del producto punto
#         imagen2[y, x] = pixel ##remplazamos los pixeles de la imagen base por la nueva posición escalada de los pixeles
        
# cv2.imshow("original", imagen) ##mostramos la imagen original
# cv2.imshow("escalada", imagen2) ##mostramos la imagen escalada

# cv2.waitKey(0)  ##esperamos que se presione una tecla
# cv2.destroyAllWindows() ##destruimos todas las ventanas referentes a opencv


#Metodo 2

imagen = cv2.imread('im1.png') ##Leemos la imagen a escalar y guardarla en la variable imagen

escalada = cv2.resize(imagen,(900,700), interpolation=cv2.INTER_CUBIC) ## interpolación bicubica
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_NEAREST) ## interpolación de vecinos cercanos
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_LINEAR) ##interpolación bilineal
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_AREA) ##muestreo usando relación de area del pixel
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_LANCZOS4) ## interpolación de lanczos en vecindario de 8x8
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_LINEAR_EXACT) ## interpolación bilineal exacta de bits

cv2.imshow('original',imagen)

cv2.imshow('escalada',escalada)

cv2.waitKey(0)
cv2.destroyAllWindows()