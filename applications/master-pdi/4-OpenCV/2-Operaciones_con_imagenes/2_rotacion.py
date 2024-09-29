# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 13:05:59 2021

@author: Jesus-Mtz
"""

import cv2
import numpy as np


imagen = cv2.imread("2.png") ## leemos la imagen a trasladar
imagen2 = cv2.resize(imagen,(200,200)) ##la redimensionamos para efectos practicos
alto, ancho, _ = imagen2.shape ##obtenemos sus medidas

angle = 70
center = (ancho//2, alto//2)
scale = .2

M = cv2.getRotationMatrix2D(center,angle,scale)
print(M)

imgT = np.zeros((alto+1,ancho+1,3),np.uint8) ##generamos una imagen base donde se guardará la imagen trasladada


for i in range(alto): ##recorremos las filas de la matriz de la imagen
    for j in range(ancho): ## recorremos las columnas de la matriz de la imagen
        try:
            px = np.array(([j,i,1]),np.uint8) 
            dot = np.dot(M,px)
            x = int((dot[0])) 
            y = int((dot[1]) )
            imgT[y,x] = imagen2[i,j] 
        except:
            pass


cv2.namedWindow("org", cv2.WINDOW_NORMAL)
cv2.namedWindow("t", cv2.WINDOW_NORMAL)

        
cv2.imshow("org", imagen2) ##mostramos la imagen redimensionada
cv2.imshow("t",imgT) ##mostramos la imagen trasladada

cv2.waitKey() ##esperamos que se presione cualquier tecla
cv2.destroyAllWindows() ##se destruyen las centanas de opencv



# import cv2
# import numpy as np


# imagen = cv2.imread("2.png") ## leemos la imagen a trasladar
# imagen2 = cv2.resize(imagen,(200,200)) ##la redimensionamos para efectos practicos
# alto, ancho, _ = imagen2.shape ##obtenemos sus medidas

# angle = 70
# center = (ancho//2, alto//2)
# scale = 1

# M = cv2.getRotationMatrix2D(center,angle,scale)


# imgT = cv2.warpAffine(imagen2,M,(ancho,alto), borderValue=(255,255,255))

# cv2.namedWindow("org", cv2.WINDOW_NORMAL)
# cv2.namedWindow("t", cv2.WINDOW_NORMAL)

# cv2.imshow("org", imagen2) ##mostramos la imagen redimensionada
# cv2.imshow("t",imgT) ##mostramos la imagen trasladada

# cv2.waitKey() ##esperamos que se presione cualquier tecla
# cv2.destroyAllWindows() ##se destruyen las centanas de opencv


# import cv2
# import numpy as np
# import imutils


# imagen = cv2.imread("2.png") ## leemos la imagen a trasladar
# imagen2 = cv2.resize(imagen,(200,200)) ##la redimensionamos para efectos practicos
# alto, ancho, _ = imagen2.shape ##obtenemos sus medidas

# angle = 70
# center = (ancho//2, alto//2)

# imgT = imutils.rotate_bound(imagen2, angle , (255,255,255))#

# cv2.namedWindow("org", cv2.WINDOW_NORMAL)
# cv2.namedWindow("t", cv2.WINDOW_NORMAL)

# cv2.imshow("org", imagen2) ##mostramos la imagen redimensionada
# cv2.imshow("t",imgT) ##mostramos la imagen trasladada

# cv2.waitKey() ##esperamos que se presione cualquier tecla
# cv2.destroyAllWindows() ##se destruyen las centanas de opencv


# import cv2
# import numpy as np

# img = cv2.imread("2.png")
# num_rows, num_cols = img.shape[:2]

# rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 1)
# img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
# cv2.imshow('Rotation', img_rotation)
# cv2.waitKey()