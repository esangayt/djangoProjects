# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:57:34 2021

@author: Jesus-Mtz
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


# img = cv2.imread('a.jpg',0) ##leemos la imagen de entrada y la guardamos en la variable img
# equ = cv2.equalizeHist(img) ##realizamos la equalización del histograma
# res = np.hstack((img,equ)) ##concatenamos la imagen de entrada con la imagen ecualizada 
# cv2.namedWindow("resultado",cv2.WINDOW_NORMAL) ##creamos la ventana con propiedad de redimencionado ya que las imagenes son algo grandes
# cv2.imshow('resultado',res) ## mostramos la imagen concatenada
# cv2.waitKey(0) ##esperamos a que se presione cualquier tecla
# cv2.destroyAllWindows() ##destruimos todas las ventanas de opencv


# hist,bins = np.histogram(img.flatten(),256,[0,256]) ##calculamos el histograma con numpy y aplanamos los datos de la imagen de entrada
# plt.hist(img.flatten(),256,[0,256], color = 'b') ##graficamos el histograma
# plt.xlim([0,256]) ##definimos limites
# plt.legend('H', loc = 'upper left') ##definimos una leyenda, en este caso H
# plt.show() ##mostramos el grafico


# hist,bins = np.histogram(res.flatten(),256,[0,256]) ##calculamos el histograma con numpy y aplanamos los datos de la imagen de entrada
# plt.hist(res.flatten(),256,[0,256], color = 'b') ##graficamos el histograma
# plt.xlim([0,256]) ##definimos limites
# plt.legend('H', loc = 'upper left') ##definimos una leyenda, en este caso H
# plt.show() ##mostramos el grafico


#CLAHE, ECUALIZACIÓON ADAPTABLE

img = cv2.imread ( 'antes.jpg' , 0) ##Leemos la imagen en escala de grises y la guardamos en la variable img

clahe = cv2.createCLAHE (clipLimit = 1.0, tileGridSize = (8,8)) ##creamos la config para el algoritmo CLAHE con un umbral de 1.0 y un kernes de 8x8

cl1 = clahe.apply (img) ##Ejecutamos el algoritmo sobre la imagen de entrada
res = np.hstack((img,cl1)) ##concatenamos la imagen de entrada con la imagen ecualizada
cv2.namedWindow("resultado",cv2.WINDOW_NORMAL) ##creamos la ventana con propiedad de redimencionado ya que las imagenes son algo grandes
cv2.imshow('resultado',res) ## mostramos la imagen concatenada
cv2.waitKey(0) ##esperamos a que se presione cualquier tecla
cv2.destroyAllWindows() ##destruimos todas las ventanas de opencv

# hist,bins = np.histogram(img.flatten(),256,[0,256]) ##calculamos el histograma con numpy y aplanamos los datos de la imagen de entrada
# plt.hist(img.flatten(),256,[0,256], color = 'r') ##graficamos el histograma
# plt.xlim([0,256]) ##definimos limites
# plt.legend('H', loc = 'upper left') ##definimos una leyenda, en este caso H
# plt.show() ##mostramos el grafico


# hist,bins = np.histogram(res.flatten(),256,[0,256]) ##calculamos el histograma con numpy y aplanamos los datos de la imagen de entrada
# plt.hist(res.flatten(),256,[0,256], color = 'r') ##graficamos el histograma
# plt.xlim([0,256]) ##definimos limites
# plt.legend('H', loc = 'upper left') ##definimos una leyenda, en este caso H
# plt.show() ##mostramos el grafico