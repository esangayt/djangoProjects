# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 14:26:11 2021

@author: Jesus-Mtz
"""

import cv2 ##importamos la libreria opencv
from matplotlib import pyplot as plt ##importamos de la libreria matplotlib su función pyplot
import numpy as np ## importamos numpy como np

img = cv2.imread ( 'lena.png' , 0) ##leemos la imagen lena.png como escala de grises y la guardamos en la variable img

##Histograma con opencv
hist = cv2.calcHist ([img], [0], None , [256], [0,255]) ## calculamos el histograma de la imagen pasando los sig paramentros
## la imagen siempre debe ir en corchetes, el canal igual en corchetes, si no vamos a usar una mascara ponemos None, secciones a dividir el histograma
## el rango de gama 0,256

##histigrama con matplotlib
plt.hist(img.ravel(), 256, [0,255])  ## graficamos el histograma, .ravel devuelve la matríz en forma plana contigua
## secciones en las cuales se divide el histograma, el rango de gama
plt.show ()


##Histograma de una imagen a color

img = cv2.imread('lena.png') ##leemos la imagen lena.png y la guardamos en la variable img

color = ('b','g','r') ##generamos la variable color y le pasamos una tupla con los indices b,g,r

for i,col in enumerate(color): ##recorremos la variable color usando un ciclo for y la función enumerate obtendriamos 0 b 1 g 2 r
    
    histr = cv2.calcHist([img],[i],None,[256],[0,256]) ## calculamos el histograma de img en cada uno de sus canales, sin mascara
    ## lo dividimos en 256 partes y en un rango de 0 a 256
    
    plt.plot(histr,color = col) ##graficamos el histograma por color
    plt.xlim([0,256]) ## definimos el rango de 0 a 256
plt.show() ## mostramos el grafico


# utilización de mascaras

img = cv2.imread('lena.png',0) ##leemos la imagen lena.png como escala de grises y la guardamos en la variable img

mask = np.zeros(img.shape[:2], np.uint8) ## creamos una imagen en engro con las dimensiones de img y la guardamos en mask

mask[0:300, 0:300] = 255 ## remplazamos los pixeles de 0 a 300 en filas y de 0 a 300 en columnas por pixeles blancos

masked_img = cv2.bitwise_and(img, img, mask = mask) ## aplicamos una compuerta and bit a bit entre img e img, pero solo en la parte de la mascara
## con pixeles blancos

hist_full = cv2.calcHist([img],[0],None,[256],[0,256]) ##calculamos el histograma completo de la imagen
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256]) ##calculamos el histograma solo del area enmascarada

plt.subplot(221), plt.imshow(img, 'gray') ## mostramos la imagen a escala de grises en una matriz de 2x2 en el espacio 1
plt.subplot(222), plt.imshow(mask,'gray') ## mostramos la mascara a escala de grises en una matriz de 2x2 en el espacio 2
plt.subplot(223), plt.imshow(masked_img, 'gray') ##mostramos el resultado de la operación bit a bit a escala de grises en el espacio 3
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask) ##mostramos los dos histrogramas en el espacio 4
plt.xlim([0,256]) ##definimos un limite en el eje x de 0 a 256 para los histogramas
plt.show() ##mostramos el grafico