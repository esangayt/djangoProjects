# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 09:23:06 2021

@author: Jesus-Mtz
"""

import numpy as np
import cv2

# ##Encontrar el centroide de los contornos

# img = cv2.imread('coins.png') ##leemos la imagen de entrada y la convertimos a escala de grises
# img2 = img.copy() ## realizamos una copia de la imagen original
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ##Convertimos la imagen original a escala de grises

# _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

# kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

# closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) ##aplicamos la función de cierre a la imagen binarizada, esto funciona 
# ## aplicando primero una dilatación y posteriormente una erosión

# contours, jerarquía = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) ##Extraemos los contornos y su jerarquia

# for index in range(len(contours)): ##recorremos el rango de la longitud de la lista de contornos, solo obtenemos el indice del contorno

#     cv2.drawContours (img2, contours, index, (0,255,0), 5) ## dibujamos cada uno de los contornos y los pintamos de verde,
#     ## con un ancho de linea de 5 px
    
#     cnt = contours[index] ##obtenemos cada uno de los contornos
#     M = cv2.moments(cnt) ##obtenemos los momentos de cada uno de los contornos
            
#     cx = int(M['m10']/M['m00']) ##calculamos la coordenada x del centroide
#     cy = int(M['m01']/M['m00']) ##calculamos la coordenada y del centroide
    
#     img = cv2.circle(img, (cx,cy), radius=2, color=(0, 0, 255), thickness=-1) ##dibujamos un punto rojo en la imagen original en el centroide
#     ##de cada contorno, el thicknes -1 significa relleno
    
#     img = cv2.putText(img, str(cx)+", "+str(cy), (cx-20,cy), cv2.FONT_HERSHEY_SIMPLEX, .3, (255,0,0), 1, cv2.LINE_AA) ##colocamos texto en la
#     ##imagen, especificamente las coordenadas x e y del centroide con fuente de .3 en azul y tamaño de linea de 1px

# cantidad = len(contours) ##obtenemos la cantidad de contornos de la imagen

# ## colocamos el texto con la cantidad de contornos en la coordenada 10 , 50
# img2 = cv2.putText(img2, 'Son '+str(cantidad)+" monedas", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

# print('Son '+str(cantidad)+" monedas") ##imprimimos la cantidad de monedas en la consola

# cv2.namedWindow("original",cv2.WINDOW_NORMAL)
# cv2.namedWindow("bordes",cv2.WINDOW_NORMAL)
# cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)  
# cv2.imshow("bordes", closing) 
# cv2.imshow("Result", img2)  
  
# cv2.waitKey(0)  
# cv2.destroyAllWindows()



##Area de un contorno

# img = cv2.imread('coins.png') ##leemos la imagen de entrada y la convertimos a escala de grises
# img2 = img.copy()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

# kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

# closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) ##aplicamos la función de cierre a la imagen binarizada, esto funciona 
# ## aplicando primero una dilatación y posteriormente una erosión

# contours, jerarquía = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# for index in range(len(contours)):

#     area = cv2.contourArea(contours[index]) ## calculamos el area de cada contorno
#     cv2.drawContours (img2, contours, index, (0,255,0), 5)
#     cnt = contours[index]
#     M = cv2.moments(cnt)
    
#     cx = int(M['m10']/M['m00'])
#     cy = int(M['m01']/M['m00'])
#     img = cv2.circle(img, (cx,cy), radius=2, color=(0, 0, 255), thickness=-1)
#     img = cv2.putText(img, str(cx)+", "+str(cy), (cx-20,cy), cv2.FONT_HERSHEY_SIMPLEX, .3, (255,0,0), 1, cv2.LINE_AA)
    
#     ## agregamos en texto el area en pixeles de cada contorno, esto en la imagen copia
#     img2 = cv2.putText(img2, str(area)+"px", (cx-20,cy), cv2.FONT_HERSHEY_SIMPLEX, .3, (255,0,0), 1, cv2.LINE_AA)

# cantidad = len(contours)

# img2 = cv2.putText(img2, 'Son '+str(cantidad)+" monedas", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

# print('Son '+str(cantidad)+" monedas")
# cv2.namedWindow("original",cv2.WINDOW_NORMAL)
# cv2.namedWindow("bordes",cv2.WINDOW_NORMAL)
# cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)  
# cv2.imshow("bordes", closing) 
# cv2.imshow("Result", img2)  
  
# cv2.waitKey(0)  
# cv2.destroyAllWindows()



##Utilizando el area de un contorno

# img = cv2.imread('contorno2.jpeg') ##leemos la imagen de entrada y la convertimos a escala de grises
# img2 = img.copy()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

# kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

# closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) ##aplicamos la función de cierre a la imagen binarizada, esto funciona 
# ## aplicando primero una dilatación y posteriormente una erosión

# contours, jerarquía = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contornosLista = [] ##creamos una lista vacia donde guardaremos los contornos
# for index in range(len(contours)):
    
#     area = cv2.contourArea(contours[index])
    
#     if area > 50000: ## condicionamos los contornos a dibujar, solo se dibujarán y procesaran los contornos con area mayor a 50000 px
#         contornosLista.append(contours[index]) ## agregamos los contornos mayores a 50000 px en la lista
        
#         cnt = contours[index]
#         M = cv2.moments(cnt)
            
#         cx = int(M['m10']/M['m00'])
#         cy = int(M['m01']/M['m00'])
#         img2 = cv2.circle(img2, (cx,cy), radius=5, color=(0, 0, 255), thickness=-1)
#         img2 = cv2.putText(img2, str(area)+"px", (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 1, cv2.LINE_AA)
        
#     cv2.drawContours (img2, contornosLista, -1, (0,255,0), 5) ## dibujamos los contornos

# cantidad = len(contornosLista)

# img2 = cv2.putText(img2, 'Son '+str(cantidad)+" contornos", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

# print('Son '+str(cantidad)+" monedas")
# cv2.namedWindow("original",cv2.WINDOW_NORMAL)
# cv2.namedWindow("bordes",cv2.WINDOW_NORMAL)
# cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)  
# cv2.imshow("bordes", closing) 
# cv2.imshow("Result", img2)  
  
# cv2.waitKey(0)  
# cv2.destroyAllWindows()
