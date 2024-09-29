# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 19:22:44 2021

@author: Jesus-Mtz
"""

import cv2

# Espacio de color RGB, rojo, verde, azul. cada canal puede variar de 0 a 255, podemos represntarlo como (255,255,255), no es la mejor opción
# para visión artificial

img = cv2.imread("1.jpeg") ##Leemos la imagen

B, G, R = cv2.split(img) ##Dividimos la imagen en sus 3 canales, Blue, Green, Red

img2 = cv2.merge((B,G,R)) ##Volvemos a unir los 3 canales de la imagen y guardamos la imagen resultante en img2

##Creación de las ventanas que usaremos para mostrar las diferentes imagenes
cv2.namedWindow("RGB",cv2.WINDOW_NORMAL)
cv2.namedWindow("R",cv2.WINDOW_NORMAL)
cv2.namedWindow("G",cv2.WINDOW_NORMAL)
cv2.namedWindow("B",cv2.WINDOW_NORMAL)
cv2.namedWindow("BGR",cv2.WINDOW_NORMAL)

##Mostramos las imagenes, original, imagenes de cada canal y la imagen compuesta
cv2.imshow("RGB", img)
cv2.imshow("R", R)
cv2.imshow("G", G)
cv2.imshow("B", B)
cv2.imshow("BGR", img2)

## Esperamos que se presione cualquier tecla
cv2.waitKey()
## destruimos todas las ventanas de opencv
cv2.destroyAllWindows()


# ##Espacio de color HSV, es mayormente utilizado para la detección de objetos mediante color

# img = cv2.imread("1.jpeg")

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) ## Convertimos la imagen BGR a hsv

# h, s, v = cv2.split(hsv) ## Dividos la imagen la imagen hsv

# cv2.imshow("HSV", hsv)
# cv2.imshow("H", h)
# cv2.imshow("S", s)
# cv2.imshow("V", v)

# ## Esperamos que se presione cualquier tecla
# cv2.waitKey()
# ## destruimos todas las ventanas de opencv
# cv2.destroyAllWindows()


# RGB to Grayscale
# img = cv2.imread("1.jpeg")

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ## Convertimos la imagen BGR a escala de grises

# cv2.imshow("grayScale", gray)

# ## Esperamos que se presione cualquier tecla
# cv2.waitKey()
# ## destruimos todas las ventanas de opencv
# cv2.destroyAllWindows()
