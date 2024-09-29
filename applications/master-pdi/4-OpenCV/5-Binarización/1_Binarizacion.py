# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:55:44 2021

@author: A.Martinez
"""

import cv2 ##importamos la librearia de opencv
from matplotlib import pyplot as plt
import numpy as np
#Es el tipo de segmentación mas sencillo y simple.
#Los pixeles de la imagen destino serán color blanco cuando los pixeles de la imagen origen superen cierto valor de umbral establecido 
#por el usuario, el resto será color negro
#La imagen resultante estará compuesta solo por pixeles blancos y negros, a esto se le llama binarizado

# img = cv2.imread("coins.png",0)

##cv2.threshold(imagen, valor de umbral, valor máximo, tipo de algoritmo de umbral), devuelve el umbral establecido y la imagen binarizada

# _, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

# cv2.imshow("original",img)
# cv2.imshow("binarizada", th)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

################################################

#binarizando con una barra de desplazamiento

# def umbral(valor): ##creamos la función para umbralizar
#     _, th = cv2.threshold(img, valor, 255, cv2.THRESH_BINARY) ## utilizamos la función threshold para realizar la binarización
#     cv2.imshow("Binarizando", th) ##mostramos la imagen binarizada

# cv2.namedWindow('Binarizando') ##creamos la ventana llamada binarizando
# img = cv2.imread("coins.png",0) ##leemos la imagen coins.png y la guardamos en la variable img

# cv2.createTrackbar("Umbral", "Binarizando", 0, 255, umbral) ##creamos un trackbar y lo adjuntamos a la ventana binarizando


# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Binarización de OTSU, en este tipo

# img = cv2.imread("coins.png",0)

# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# plt.hist(img.ravel(), 256, [0,255]) ## graficamos el histograma, .ravel nos devuelve la matriz en fpormato plano
# plt.show()

# ##cv2.threshold(imagen, valor de umbral, valor máximo, tipo de algoritmo de umbral), devuelve el umbral establecido y la imagen binarizada

# umbral, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# print(umbral)

# cv2.imshow("original",img)
# cv2.imshow("binarizada", th)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

################################################

##Binarización adaptativa

kernel = 3 ##definimos las dimensiones del kernel
constante =0 ##definimos la constante

def updateKernel(krn): ##creamos la función updateKernel y le pasamos krn
    global kernel ##hacemos global la variable kernel
    kernel = krn ##pasamos el valor de krn a la variable kernel
    
    if kernel < 3 : ##si kernel es menor a 3, kernel se volverá 3
        kernel = 3
    elif kernel %2 == 0: ##si kernel es un valor par, le sumamos 1 para volverlo impar
        kernel +=1
    
    ## aplicamos una umbralización adaptativa gaussiana a la imagen de entrada y le pasamos los valores de kernel y constante
    umbralizada = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, kernel, constante)
    
    # umbralizada = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel, constante)
    
    cv2.imshow("Binarizada", umbralizada)## mostamos la imagen umbralizada en la ventana binarizada

def updateConstante(cte): ## creamos la función updateConstante y le pasamos cte
    global constante ## hacemos global la variable constante
    constante = cte ## pasamos el valor de cte a la variable constante
    
    ## aplicamos una umbralización adaptativa gaussiana a la imagen de entrada y le pasamos los valores de kernel y constante
    umbralizada = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, kernel, constante)
    
    # umbralizada = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel, constante)
    cv2.imshow("Binarizada", umbralizada) ## mostamos la imagen umbralizada en la ventana binarizada
    
cv2.namedWindow('Binarizada') ##creamos la ventana llamada binarizando
img = cv2.imread("coins.png", 0) ##leemos la imagen coins,png como escala de grises y la guardamos en la variable img

##creamos una barra de desplazamiento llamada kernel en la ventana binarizada, la inicializamos en 3 y cada movimiento realizado manda 
##llamar la función updateKernel y le pasa el valor del trackBar en krn
cv2.createTrackbar("kernel", "Binarizada", kernel, 255, updateKernel)

##creamos una barra de desplazamiento llamada constante en la ventana binarizada, la inicializamos en 0 y cada movimiento realizado manda 
##llamar la función updateConstante y le pasa el valor del trackBar en cte
cv2.createTrackbar("constante", "Binarizada", constante, 255, updateConstante)

cv2.waitKey(0) ##esperamos que se presione cualquier tecla
cv2.destroyAllWindows() ##destruimos las ventanas de opencv


##Binarización adaptativa

# kernel = 3
# constante =2
    
# cv2.namedWindow('Binarizada') ##creamos la ventana llamada binarizando
# img = cv2.imread("coins.png", 0) ##leemos la imagen coins.png como escala de grises y la guardamos en la variable img

# ## aplicamos una umbralización adaptativa gaussiana a la imagen de entrada y le pasamos los valores de kernel y constante
# umbralizada = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, kernel, constante)

# # umbralizada = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel, constante)

# cv2.imshow("Binarizada", umbralizada)## mostamos la imagen umbralizada en la ventana binarizada

# cv2.waitKey(0) ##esperamos que se presione cualquier tecla
# cv2.destroyAllWindows() ##destruimos las ventanas de opencv