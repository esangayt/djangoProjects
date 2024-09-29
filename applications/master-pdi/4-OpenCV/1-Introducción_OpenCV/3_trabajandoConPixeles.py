# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 20:14:03 2021

@author: Jesus-Mtz
"""

import cv2  
import numpy as np

imagenObscura = np.zeros((100,100,3), np.uint8) ##creamos una matríz numpy de 3 dimenciones y la rellenamos con ceros

pixel = imagenObscura[97,97] ##Leemos el valor del pixel en la posición 97, 97, de la matríz en general, nos devolvera un vector de 3 elementos

print(type(pixel)) ##mostramos en consola el valor contenido en ese pixel

imagenObscura[97,97] = [255,255,255] ##remplazamos el valor del pixel de la posición 97, 97 por un pixel blanco


##obtener los valores de cada pixel de la imagen:

## obtenemos las dimenciones de la imagen creada, esto con shape. filas, columnas y canales
alto, largo, _ = imagenObscura.shape

##Recorremos la imagen imprimiendo los valores de cada pixel
for i in range(largo):
    for j in range(alto):
        print(imagenObscura[i,j])
        
##Modificar los valores de cada pixel:
for i in range(largo):
    for j in range(alto):
        pixel = imagenObscura[i,j]
        if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
            imagenObscura[i,j] = [125,125,200]

cv2.namedWindow("black",cv2.WINDOW_NORMAL)
cv2.imshow("black", imagenObscura)

cv2.waitKey()

cv2.destroyAllWindows()



# ##Leemos la imagen de entrada
# img = cv2.imread("candados.jpg")

# # ## obtenemos las dimenciones de la imagen, esto con shape. filas, columnas y canales
# alto, largo, _ = img.shape
# print(largo, alto)

# candado1 = img[0:alto, 0:int(largo/2)] ## obtenemos los pixeles comprendidos desde el inicio de la imagen a lo ancho, hasta la mitad de la misma
# ## y los de su altura completa, generando una imagen nueva, llamada candado 1

# ## adquirimos los pixeles desde la mitad de la imagen a lo ancho, hasta el final. a su vez el total de su alto, con esto generamos
# ## una imagen nueva llamada candado 2
# candado2 = img[0:alto, int(largo/2):]

# imagenCompuesta = np.zeros((alto,largo,3), np.uint8) ##creamos una matríz numpy de 3 dimenciones y la rellenamos con ceros

# alto, largo, _ = imagenCompuesta.shape ##obtenemos las dimensiones de la imagen solo para comprobar
# print(largo, alto)

# imagenCompuesta[0:alto, 0:int(largo/2)] = candado2 ##asignamos la imagen candado 2 a los pixeles correspondientes al candado1
# imagenCompuesta[0:alto, int(largo/2):] = candado1 ##asignamos la imagen candado 1 a los pixeles correspondientes al candado 2


# cv2.namedWindow("original",cv2.WINDOW_NORMAL)
# cv2.namedWindow("candado1",cv2.WINDOW_NORMAL)
# cv2.namedWindow("candado2",cv2.WINDOW_NORMAL)
# cv2.namedWindow("compuesta",cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)
# cv2.imshow("candado1", candado1)
# cv2.imshow("candado2", candado2)
# cv2.imshow("compuesta", imagenCompuesta)

# cv2.waitKey()

# cv2.destroyAllWindows()


#Selección mediante mouse

# # ##Leemos la imagen de entrada
# img = cv2.imread("candados.jpg")

# ##Generamos una copia de la imagen original
# imgcopy = img.copy()

# # ## obtenemos las dimenciones de la imagen, esto con shape. filas, columnas y canales
# alto, largo, _ = img.shape
# print(largo, alto)

# cv2.namedWindow("roi",cv2.WINDOW_NORMAL) ##Generamos la ventana para la selección del roi

# roi1=cv2.selectROI("roi", img) ##Llamamos la función selectRoi y le pasamos el nombre de la ventana y la imagen
# print(roi1)

# ##extraemos de la imagen original el fragmento correspondiente a la roi1
# candado1 = img[int(roi1[1]):int(roi1[1]+roi1[3]), int(roi1[0]):int(roi1[0]+roi1[2])]
# alto1, largo1, _ = candado1.shape

# roi2=cv2.selectROI("roi", img) ##Llamamos la función selectRoi y le pasamos el nombre de la ventana y la imagen
# print(roi2)

# ##extraemos de la imagen original el fragmento correspondiente a la roi2
# candado2 = img[int(roi2[1]):int(roi2[1]+roi2[3]), int(roi2[0]):int(roi2[0]+roi2[2])]
# alto2, largo2, _ = candado2.shape

# newCandado1 = cv2.resize(candado1, (largo2, alto2)) ##redimencionamos el candado 1 con las medidas del candado 2 y lo guardams en newcandado1

# newCandado2 = cv2.resize(candado2, (largo1, alto1)) ##redimencionamos el candado 2 con las medidas del candado 1 y lo guardams en newcandado2

# ## verificamos las medidas de las nuevas imagenes
# alto1, largo1, _ = newCandado1.shape
# print(alto1, largo1)
# alto1, largo1, _ = newCandado2.shape
# print(alto1, largo1)


# ##Remplazamos los fragmentos correspondientes a cada roi con su imagen contraria en la imagen copia
# imgcopy[int(roi1[1]):int(roi1[1]+roi1[3]),int(roi1[0]):int(roi1[0]+roi1[2])] = newCandado2 
# imgcopy[int(roi2[1]):int(roi2[1]+roi2[3]), int(roi2[0]):int(roi2[0]+roi2[2])] = newCandado1


# cv2.namedWindow("original",cv2.WINDOW_NORMAL)
# cv2.namedWindow("candado1",cv2.WINDOW_NORMAL)
# cv2.namedWindow("candado2",cv2.WINDOW_NORMAL)
# cv2.namedWindow("compuesta",cv2.WINDOW_NORMAL)
# cv2.namedWindow("compuesta2",cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)
# cv2.imshow("candado1", candado1)
# cv2.imshow("candado2", candado2)
# cv2.imshow("compuesta", imgcopy)

# ##Generando la imagen original mediante una imagen compuesta
# newCandado2 = cv2.resize(candado2, (largo2, alto2)) ##redimencionamos el candado 2 con las medidas del candado 2 y lo guardams en newcandado2
# newCandado1 = cv2.resize(candado1, (largo1, alto1)) ##redimencionamos el candado 1 con las medidas del candado 1 y lo guardams en newcandado1

# imgcopy[int(roi1[1]):int(roi1[1]+roi1[3]),int(roi1[0]):int(roi1[0]+roi1[2])] = newCandado1
# imgcopy[int(roi2[1]):int(roi2[1]+roi2[3]), int(roi2[0]):int(roi2[0]+roi2[2])] = newCandado2

# cv2.imshow("compuesta2", imgcopy)

# cv2.waitKey()

# cv2.destroyAllWindows()










