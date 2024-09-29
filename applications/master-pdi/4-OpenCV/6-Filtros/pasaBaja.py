# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:02:27 2021

@author: Jesus-Mtz
"""

import cv2
import numpy as np
##Filstros pasa baja:
    
#Filtro de promediado

# img = cv2.imread("salYpimienta.jpg", 0) ##Leemos la imagen sal y pimienta en escala de grises y la guardamos en img

# imgBlurred = cv2.blur(img,(8,8)) ##aplicamos un filtro de promediado con un kernel de 8 x 8 a la imagen original y la guardamos en imgBlurred

# cv2.imshow("original", img) ##mostramos la imagen original
# cv2.imshow("blurred", imgBlurred) ##mostramos la imagen difuminada

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Filtro de desenfoque Gaussiano

# img = cv2.imread("images.jpg", 0) ## cargamos la imagen como escala de grises y la guardamos en img 

# ##GaussianBlur(imagen de entrada, imagen de salida, tamaño del kernel, sigmaX, sigmaY)
# imgBlurred = cv2.GaussianBlur(img,(9,9),0) ## aplicamos el desenfoque gaussiano

# cv2.imshow("original", img) ##mostramos la imagen original
# cv2.imshow("blurred", imgBlurred) ## mostramos la imagen con desenfoque gaussiano

# cv2.waitKey(0)
# cv2.destroyAllWindows()


##Filtro de desenfoque medio:
    

# img = cv2.imread("images.jpg", 0) ## cargamos la imagen como escala de grises y la guardamos en img 

# median = cv2.medianBlur(img,7) ## aplicamos el filtro de media con un kernel de 7 x 7 en la imagen 

# cv2.imshow("original", img) ##mostramos la imagen original
# cv2.imshow("blurred", median) ## mostramos la imagen con desenfoque gaussiano

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# filtrado bilateral:
   
# img = cv2.imread("images.jpg", 0) ## cargamos la imagen como escala de grises y la guardamos en img 

# blur = cv2.bilateralFilter(img,9,75,75)

# cv2.imshow("original", img) ##mostramos la imagen original
# cv2.imshow("blurred", blur) ## mostramos la imagen con desenfoque gaussiano

# cv2.waitKey(0)
# cv2.destroyAllWindows()




img = cv2.imread('a.jpg',0) ##leemos la imagen de entrada y la guardamos en la variable img
equ = cv2.equalizeHist(img) ##realizamos la equalización del histograma

blur = cv2.blur(equ,(8,8)) ##aplicamos un filtro de promediado con un kernel de 8 x 8 a la imagen original y la guardamos en imgBlurred
# blur = cv2.GaussianBlur(blur,(5,5),0) ## aplicamos el desenfoque gaussiano
blur = cv2.medianBlur(blur,3)

sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

res = np.hstack((img,equ,blur,sharpen)) ##concatenamos la imagen de entrada con la imagen ecualizada 


cv2.namedWindow("resultado",cv2.WINDOW_NORMAL) ##creamos la ventana con propiedad de redimencionado ya que las imagenes son algo grandes
cv2.imshow('resultado',res) ## mostramos la imagen concatenada
cv2.waitKey(0) ##esperamos a que se presione cualquier tecla
cv2.destroyAllWindows() ##destruimos todas las ventanas de opencv


