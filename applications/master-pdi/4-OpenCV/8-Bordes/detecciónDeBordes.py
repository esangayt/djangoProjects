# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:32:40 2021

@author: Jesus-Mtz
"""

import cv2  
import numpy as np    

#Filtro sobel
  
img = cv2.imread("coins.png", 0)  ## leemos la imagen de entrada en escala de grises y la guardamos en img
  
x = cv2.Sobel(img,cv2.CV_16S,1,0,ksize = 3) ##aplicamos el filtrado Sobel con una derivada de grado 1 en X y un kernel de 3x3, se convierte la imagen a 16 bits
y = cv2.Sobel(img,cv2.CV_16S,0,1,ksize = 3)  ##aplicamos el filtrado Sobel con una derivada de grado 1 en Y y un kernel de 3x3, se convierte la imagen a 16 bits
  
absX = cv2.convertScaleAbs(x) #Convertimos los valores obtenidos en valores absolutos y la salida de esta función nos retorna la imagen en 8 bits
absY = cv2.convertScaleAbs(y) #Convertimos los valores obtenidos en valores absolutos y la salida de esta función nos retorna la imagen en 8 bits
  
dst = cv2.addWeighted(absX,0.5,absY,0.5,0) ##combinamos las dos imagenes, definiendo a 0.5 el peso de los elementos en la primer imagen
## y en 0.5 los pesos de la segunda, el tercero es solo un valor agregado, que realizamos con esta función, en pocas palabras la combinación
#de ambas imagenes con una transparencia de 0.5 para ambas.
  
cv2.imshow("absX", absX)  
cv2.imshow("absY", absY)  
  
cv2.imshow("Result", dst)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()  

#########################################################################################

# Filtro Canny
#Su aplicación en codigo es demasciado sencilla,

img = cv2.imread('coins.png',0) ##leemos la imagen de entrada y la convertimos a escala de grises
bordes = cv2.Canny(img,135,255) ## aplicamos el filtro canny para la detección de bordes seleccionamos un umbral minimo de 135 y un maximo de 255

cv2.imshow("Result", bordes)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()

############################################################################################

""" ok una vez realizada la aplicación de un filtro canny, podemos aplicarlo en algo un poco mas complejo, en este caso vamos a limpiar el interior de la imagen
esto eliminará bordes que no necesito en la imagen en estos momentos, vamos a realizarlo.
"""

img = cv2.imread('coins.png',0) ##leemos la imagen de entrada y la convertimos a escala de grises
# gaussiana = cv2.bilateralFilter(img,7, 80, 80)
gaussiana = cv2.GaussianBlur(img, (9,9), 0) ## aplicamos un filtro gaussiano con kernel de 9 por 9

_, th = cv2.threshold(gaussiana, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 5, 5), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

bordes = cv2.Canny(th,135,255) ## aplicamos el filtro canny para la detección de bordes seleccionamos un umbral minimo de 135 y un maximo de 255

cv2.imshow("Result", bordes)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()

################################################################################################################

""" Una vez que hemos visto como eliminar bordes indeseables en la imagen, vamos a proceder a remarcar los bordes de la imagen brindandoles otro color
por ejemplo color verde,

"""

imgC = cv2.imread('coins.png') ##leemos la imagen de entrada y la convertimos a escala de grises
imgD = imgC.copy()
img = cv2.cvtColor(imgC, cv2.COLOR_BGR2GRAY)
alto, largo= img.shape
# gaussiana = cv2.bilateralFilter(img,7, 80, 80)
gaussiana = cv2.GaussianBlur(img, (9,9), 0)

_, th = cv2.threshold(gaussiana, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

# kernel  =  np.ones (( 5, 5), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

bordes = cv2.Canny(th,135,255) ## aplicamos el filtro canny para la detección de bordes seleccionamos un umbral minimo de 135 y un maximo de 255

for i in range(largo):
    for j in range(alto):
        if bordes[j,i] == 255:
            imgD[j,i] = (0,255,0)

cv2.imshow("Original", imgC)           
cv2.imshow("Bordes", bordes)  
cv2.imshow("Result", imgD)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()


####################################################################################################


imgC = cv2.imread('coins.png') ##leemos la imagen de entrada y la convertimos a escala de grises
imgD = imgC.copy()
img = cv2.cvtColor(imgC, cv2.COLOR_BGR2GRAY)
alto, largo= img.shape


_, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) ##binarizamos la imagen de entrada y la guardamos en th

kernel  =  np.ones (( 3, 3), np.uint8 )  ## construimos un kernel de 3x3 de solo unos

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel) ##aplicamos la función de cierre a la imagen binarizada, esto funciona 
# ## aplicando primero una dilatación y posteriormente una erosión

bordes = cv2.Canny(closing,135,255) ## aplicamos el filtro canny para la detección de bordes seleccionamos un umbral minimo de 135 y un maximo de 255

for i in range(largo):
    for j in range(alto):
        if bordes[j,i] == 255:
            imgD[j,i] = (0,255,0)

cv2.imshow("Original", imgC)           
cv2.imshow("Bordes", bordes)  
cv2.imshow("Result", imgD)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()




