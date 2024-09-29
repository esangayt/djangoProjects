# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:58:11 2021

@author: Jesus-Mtz
"""

import cv2
import numpy as np

img = cv2.imread('engranaje.jpg',0)
img2 = img.copy()
template = cv2.imread('template.jpg',0)
w, h = template.shape[::-1]


methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    cv2.imwrite(meth+".jpg",img)



img_rgb = cv2.imread('waldo.jpg') ## cargamos nuestra imagen rgb
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) ##convertimos la imagen rgb a escala de grises
template = cv2.imread('waldotemplate.jpg',0) ## cargamos nuestro template en escala de grises

w, h = template.shape[::-1] ## obtenemos las medidas de nuestra imagen template y las mostramos a la inversa

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) ## realizamos el proceso de comparación de plantillas  en la imagen en escala de grises

threshold = 0.8 ## definimos un umbral minimo de 80% de coincidencia para la detección del objeto
rectangulos = np.where(res >= threshold) ## realizamos la comparación de resultados, y evaluamos cada elemento de la matríz
## si el valor en la matríz es mayor o igual al umbral, lo agregamos a rectangulos
# print(rectangulos)
for pt in zip(*rectangulos[::-1]): ##recorremos los elementos de rectangulos a la inversa, los emparejamos y los guardamos en tuplas
    print(pt)
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2) ##dibujamos el rectangulo resultante

cv2.imshow("resultado", img_rgb) ##mostramos la imagen modificada

cv2.waitKey()
cv2.destroyAllWindows()



#Matching con umbral variable mediante trackBar

def umbral(valor):
    img2 = img_rgb.copy()
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = valor/100
    rectangulos = np.where(res >= threshold)

    for pt in zip(*rectangulos[::-1]):
        print(pt)
        cv2.rectangle(img2, pt, (pt[0] + w, pt[1] + h), (0,255,0), 1)
    cv2.imshow("match", img2)

cv2.namedWindow('match',cv2.WINDOW_NORMAL)

img_rgb = cv2.imread('engranaje.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.jpg',0)
cv2.imshow("match", img_rgb)

cv2.createTrackbar("Umbral", "match", 0, 100, umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ##Seleccionar elemento a buscar mediante ROISelect

def umbral(valor):
    img2 = img_rgb.copy()
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = valor/100
    rectangulos = np.where(res >= threshold)
    print(rectangulos)

    for pt in zip(*rectangulos[::-1]):
        # print(pt)
        cv2.rectangle(img2, pt, (pt[0] + w, pt[1] + h), (0,255,0), 1)
    cv2.imshow("match", img2)

cv2.namedWindow('match',cv2.WINDOW_NORMAL)

img_rgb = cv2.imread('engranaje.jpg')
roi = cv2.selectROI('match', img_rgb, False)
x = roi[0]
y = roi[1]
w = roi[2]
h = roi[3]

template = img_rgb[y:y+h, x:x+w]

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.imshow("match", img_rgb)

cv2.createTrackbar("Umbral", "match", 0, 100, umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()

