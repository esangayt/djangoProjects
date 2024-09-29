# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:52:28 2021

@author: Jesus-Mtz
"""

import cv2 ## importamos la libreria opencv

# img1 = cv2.imread('1.png') ##leemos la imagen 1 y la guardamos en img1
# img1 = cv2.resize(img1,(500,500))

# img2 = cv2.imread('2.png') ## leemos la imagen 2 y la guardamos en img2
# img2 = cv2.resize(img2,(500,500))

# resultadoSuma = cv2.add(img1,img2) ## realizamos la suma de imagenes
# resultadoResta = cv2.subtract(img2,img1) ## realizamos la resta de imagenes

# resultadoDivision = cv2.divide(img1,img2) ## realizamos la división de imagenes
# resultadoMultiplicacion = cv2.multiply(img1,img2) ## realizamos la multiplicación de imagenes

# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
# cv2.imshow('resultadoSuma',resultadoSuma)
# cv2.imshow('resultadoResta',resultadoResta)
# cv2.imshow('resultadoDivision',resultadoDivision)
# cv2.imshow('resultadoMultiplicacion',resultadoMultiplicacion)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# por ejemplo la resta de imagenes es altamente utilizable en la detección de movimiento para sistemas de vigilancia,
#podemos tomar el frame pasado de una imagen y restarle el frame actual, en caso de que exista una variación, este nos lo resaltará

#Ejemplo con diferencia absoluta
    
# import cv2 ## importamos la libreria opencv

# img1 = cv2.imread('casaVacia.jpg') ##leemos la imagen 1 y la guardamos en img1
# img1 = cv2.resize(img1,(500,500))

# img2 = cv2.imread('casaDibujo.jpg') ## leemos la imagen 2 y la guardamos en img2
# img2 = cv2.resize(img2,(500,500))

# resultadoResta = cv2.absdiff(img2,img1) ## realizamos la resta de imagenes

# cv2.imshow('resultadoResta',resultadoResta)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Detección de movimiento


cap = cv2.VideoCapture(1) ##obtenemos la captura de una webcam

f = 0 ##inicializamos un conteo

while True: #mientras sea verdadero se ejecuta ciclo while
    
  ret, frame = cap.read() ##de la lectura de la captura de la camara, vamos a extraer el frame o imagen capturada
  
  gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ##convertimos a escala de grises la imagen capturada
  
  if f == 10: ## si el conteo es igual a 10 asignale la imagen en escala de grises a la variable fonto
    fondo = gris ##asignación de variable
    
  if f > 10: ## si el conteo es mayor a 10 realiza lo contenido dentro del if
    dif = cv2.absdiff(gris, fondo) ## obtenemos la diferencia absolta de la imagen capturada actual y del fondo
    
    _, th = cv2.threshold(dif, 15, 255, cv2.THRESH_BINARY) ##realizamos una binarización con 15 de valor de umbral
    
    contornos, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) ## obtenemos los contornos de la imagen
    
    for c in contornos: ##recorremos los contornos obtenidos
        
      area = cv2.contourArea(c) ## calculamos el area de cada contorno obtenido
      
      if area > 200: ## si el area es mayor a 200 pixeles, hacer lo contenido en el if
        x,y,w,h = cv2.boundingRect(c) ##obtenemos las coordenadas de un rectangulo a partir del contorno
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)  ## dibujamos un rectangulo al rededor del contorno
        
  cv2.imshow('Frame',frame) ## mostramos el frame modificado con los rectangulos dibujados
  
  f = f+1 ## aumentamos la cuenta en 1
  
  
  
  
  
  
  
  
  
  
  
  
  if cv2.waitKey(1) & 0xFF == ord ('q'):
    break

cap.release()
cv2.destroyAllWindows()
