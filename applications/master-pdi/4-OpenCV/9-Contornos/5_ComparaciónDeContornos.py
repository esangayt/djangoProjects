# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:49:09 2021

@author: Jesus-Mtz
"""
"""Ok, vamos a realizar una comparacion de contornos, el ejercicio es muy simple, vamos a leer dos imagenes
una imagen sera nuestro template o base, la segunda sera la imagen a comparar, las convertiremos en escala de
grises, posteriormente las binarizaremos y aplicaremos operaciones morfologicas, ya en este punto aplicaremos
una extraccion de contornos, estos contornos los almacenaremos en una lista, utilizaremos una lista por
imagen, una vez realizado esto compararemos cada uno de estos contornos entre si y sumaremos sus resultados para
asi calcular el grado de similitud entre los contornos de cada imagen, veamoslo."""

import cv2
import numpy as np

img = cv2.imread('gear1.png')
img2 = cv2.imread('gear2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, th2 = cv2.threshold(gray2, 150, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel  =  np.ones (( 5, 5), np.uint8 )
closingImg = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
closingImg2 = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel)

contours, jerarquia = cv2.findContours(closingImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, jerarquia2 = cv2.findContours(closingImg2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contornosLista = []
for index in range(len(contours)):
    area = cv2.contourArea(contours[index])
    if area > 500 :
        cnt = contours[index]
        contornosLista.append(cnt)

contornosLista2 = []
for index in range(len(contours2)):
    area = cv2.contourArea(contours2[index])
    if area > 500:
        cnt = contours2[index]
        contornosLista2.append(cnt)

cv2.drawContours (img2, contornosLista2, -1, (0,255,0), 1)
cv2.drawContours (img, contornosLista, -1, (0,255,0), 1)

suma = 0.0
for index in range(len(contornosLista)):
    ret = cv2.matchShapes (contornosLista[index], contornosLista2[index],1,0.0)
    suma += ret

if suma > 0.0009:
    img2 = cv2.putText(img2, "No iguales", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)
else:
    img2 = cv2.putText(img2, "OK", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)

cv2.namedWindow("testeando",cv2.WINDOW_NORMAL)
cv2.namedWindow("original",cv2.WINDOW_NORMAL)
cv2.imshow("testeando", img2)
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()