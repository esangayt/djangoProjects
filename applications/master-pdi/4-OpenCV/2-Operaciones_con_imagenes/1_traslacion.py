# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:56:02 2021

@author: Jesus-Mtz
"""

import numpy as np
import cv2


imagen = cv2.imread("1.jpg") ## leemos la imagen a trasladar
imagen2 = cv2.resize(imagen,(100,50)) ##la redimensionamos para efectos practicos
alto, ancho, _ = imagen2.shape ##obtenemos sus medidas
print(alto)
tx = 10 ##definimos la traslación en x
ty = 2 ## definimos la traslación en y

mT = np.array(([1,0,tx],[0,1,ty],[0,0,1]),np.uint8) ##creamos nuestra matríz de transformación

imgT = np.zeros((alto+2,ancho+10,3),np.uint8) ##generamos una imagen base donde se guardará la imagen trasladada


for i in range(alto): ##recorremos las filas de la matriz de la imagen
    for j in range(ancho): ## recorremos las columnas de la matriz de la imagen

        px = np.array(([j,i,1]),np.uint8) ##formamos nuestro vector [px,py,1]
        dot = np.dot(mT,px) ##aplicamos producto punto entre la matriz de transformación y el vector del pixel
        x = dot[0] ##extraemos el valor para x
        y = dot[1] ## extraemos el valor para y
        imgT[y,x] = imagen2[i,j] ## remplazamos los valores de los pixeles

cv2.namedWindow("org",cv2.WINDOW_NORMAL)
cv2.namedWindow("t",cv2.WINDOW_NORMAL)
cv2.imshow("org", imagen2) ##mostramos la imagen redimensionada
cv2.imshow("t",imgT) ##mostramos la imagen trasladada

cv2.waitKey() ##esperamos que se presione cualquier tecla
cv2.destroyAllWindows() ##se destruyen las centanas de opencv


# # otra forma de realizarlo

imagen = cv2.imread("1.jpg") ## leemos la imagen a trasladar
imagen2 = cv2.resize(imagen,(100,50)) ## redimensionamos para efectos practicos
alto, ancho, _ = imagen2.shape ##obtenemos las dimensiones de la imagen

tx = 20 ##definimos el desplazamiento en x
ty = 2 ##definimos el desplazamiento en y

mT = np.array(([1,0,tx],[0,1,ty],[0,0,1]),np.uint8) ##generamos la matriz de traslación

imgT = np.zeros((alto+ty,ancho+tx,3),np.uint8) ##generamos la imagen en la cual se va a guardar la imagen trasladada


for i in range(alto): ##recorremos las filas
    for j in range(ancho): ##recorremos las columnas
        x = j+tx ##sumamos el desplazamiento en x al indice de las columnas
        y = i+ty ##sumamos el desplazamiento en y al indice de las filas
        imgT[y,x] = imagen2[i,j] ## remplazamos los pixeles en las imagenes

cv2.namedWindow("org",cv2.WINDOW_NORMAL)
cv2.namedWindow("t",cv2.WINDOW_NORMAL)

cv2.imshow("org", imagen2) ##mostramos la imagen redimensionada
cv2.imshow("t",imgT) ##mostramos la imagen trasladada

cv2.waitKey() ##esperamos que se presione cualquier tecla
cv2.destroyAllWindows() ##se destruyen las centanas de opencv


##la forma rapida con opencv

# imagen = cv2.imread('1.jpg') ##leemos la imagen a trasladar

# # Store height and width of the image
# height, width = imagen.shape[:2] #obtenemos las dimenciones de la imagen

# mT = np.float32([[1, 0, 100], [0, 1, 2]]) ##generamos la matriz de transformación

# ## utilizamos la función cv2.warpAffine(), esta recibe la imagen a trasladar, la matríz de transformación y las dimensiones originales de la imagen
# ##a trasladar, nos devuelve la imagen con la traslación aplicada
# imgT = cv2.warpAffine(imagen, mT, (width, height))

# cv2.imshow("org", imagen) ##mostramos la imagen redimensionada
# cv2.imshow("t",imgT) ##mostramos la imagen trasladada

# cv2.waitKey() ##esperamos que se presione cualquier tecla
# cv2.destroyAllWindows() ##se destruyen las centanas de opencv