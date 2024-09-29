# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 10:46:11 2021

@author: Jesus-Mtz
"""

import cv2
import numpy as np


# tMatrix = np.array([[1,0,0],[1,1,0],[0,1,1]]) ## Creamos la matriz de transformación y la guardamos en tMatrix
# mResultante = np.zeros((500, 500,3),np.uint8) ##Creamos la matriz resultante en la que guardaremos la imagen transformada

# imagen = cv2.imread("1.png")   ## Leemos la imagen a transformar y la guardamos en la variable imagen

# h,w,_ = imagen.shape ## obtenemos las dimensiones altura y ancho de la imagen de entrada y las guardamos en h y w respectivamente

# for i in range(h): ## recorremos la altura de la imagen
#     for j in range(w): ##recorremos el ancho de la imagen
#         pixel = imagen[i,j] ## creamos el pixel que incrustaremos en la imagen transformada
#         vector = np.array([j,i,1]) ## generamos el vector a transformar
#         result = np.dot(tMatrix,vector) ## aplicamos producto punto entre la matriz de transformación y el vector
#         x = result[0] ## extraemos el componente x del vector resultante
#         y = result[1]   ## extraemos el componente y del vector resultante
#         mResultante[y, x] = pixel ## remplazamos el pixel original en la imagen transformada

# cv2.imshow("original", imagen) ## mostramos la imagen original
# cv2.imshow("escalada", mResultante) ## mostramos la imagen resultante

# cv2.waitKey(0) ## esperamos que se presione cualquier tecla
# cv2.destroyAllWindows() ## destruimos las ventanas de opencv



# tMatrix = np.array([[1,1,0],[0,1,0],[0,1,1]]) ## Creamos la matriz de transformación y la guardamos en tMatrix
# mResultante = np.zeros((500, 500,3),np.uint8) ##Creamos la matriz resultante en la que guardaremos la imagen transformada
# imagen = cv2.imread("1.png") ## Leemos la imagen a transformar y la guardamos en la variable imagen

# h,w,_ = imagen.shape ## obtenemos las dimensiones altura y ancho de la imagen de entrada y las guardamos en h y w respectivamente

# for i in range(h): ## recorremos la altura de la imagen
#     for j in range(w): ##recorremos el ancho de la imagen
#         pixel = imagen[i,j] ## creamos el pixel que incrustaremos en la imagen transformada
#         vector = np.array([j,i,1]) ## generamos el vector a transformar
#         result = np.dot(tMatrix,vector) ## aplicamos producto punto entre la matriz de transformación y el vector
#         x = result[0] ## extraemos el componente x del vector resultante
#         y = result[1] ## extraemos el componente y del vector resultante
#         mResultante[y, x] = pixel  ## remplazamos el pixel original en la imagen transformada

# cv2.imshow("original", imagen) ## mostramos la imagen original
# cv2.imshow("escalada", mResultante) ## mostramos la imagen resultante

# cv2.waitKey(0) ## esperamos que se presione cualquier tecla
# cv2.destroyAllWindows() ## destruimos las ventanas de opencv


img=cv2.imread('TESLA.jpEg')
rows,cols,ch=img.shape

cv2.namedWindow("imagen1", cv2.WINDOW_NORMAL)

global listaPuntos
listaPuntos = []
def getPoints(event, x,y,flags, params):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        listaPuntos.append([x,y])


cv2.setMouseCallback("imagen1", getPoints)
cv2.imshow("imagen1", img)

while True:
    if cv2.waitKey(0) == 13:
        print(listaPuntos)
        pts1 = np.float32(listaPuntos)
        pts2 = np.float32([[0,0],[cols,0],[0,rows],[cols,rows]])
        M=cv2.getPerspectiveTransform(pts1,pts2)
        dst=cv2.warpPerspective(img,M,(cols,rows))
        cv2.imshow("imagen1", dst)

    if cv2.waitKey(0) == 27:
        break

print(listaPuntos)
cv2.destroyAllWindows()