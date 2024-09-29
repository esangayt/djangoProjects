# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 17:39:50 2021

@author: Jesus-Mtz
"""
##importamos la libreria OpenCV usando import cv2

import cv2

# ##Utilizando el comando imread de opencv leeremos la imagen 1.jpeg y la guardaremos en la variable img
# img = cv2.imread("1.jpeg")

# #utilizando el comando imshow de opencv mostraremos la imangen en una ventana llamda ventana
# cv2.imshow("ventana", img)

# ##Controla el tiempo de muestreo de la señal de entrada por teclado
# cv2.waitKey()

# ##Cierra todas las ventanas creadas por OpenCV
# cv2.destroyAllWindows()

# ##Guardamos la imagen contenida en la variable img en el archivo imagenGuardada1.jpeg
# cv2.imwrite("imagenGuardada1.jpeg", img)




# ##Agregando IMREAD_GRAYSCALE podemos leer la imagen en escala de grises
# img = cv2.imread("1.jpeg", cv2.IMREAD_GRAYSCALE)

# #utilizando el comando imshow de opencv mostraremos la imangen en una ventana llamda ventana
# cv2.imshow("ventanaGrayScale", img)

# ##Controla el tiempo de muestreo de la señal de entrada por teclado
# cv2.waitKey()

# ##Cierra todas las ventanas creadas por OpenCV
# cv2.destroyAllWindows()

# ##Guardamos la imagen contenida en la variable img en el archivo imagenGuardada1.jpeg
# cv2.imwrite("imagenGuardadaGray1.png", img)



##Jugando con waitKey()

# img = cv2.imread("1.jpeg")
# img2 = cv2.imread("1.jpeg", cv2.IMREAD_GRAYSCALE)

# while True:
#     cv2.imshow("color", img)
#     cv2.imshow("grises", img2)
    
#     key = cv2.waitKey()
    
#     if key == ord("g"):
#         cv2.imwrite("imagenGuardada.png", img)
    
#     elif key == ord("G"):
#         cv2.imwrite("imagenGuardada2.png", img)
#     else:
#         break
    
# cv2.destroyAllWindows()



img = cv2.imread("1.jpeg")
img2 = cv2.imread("1.jpeg", cv2.IMREAD_GRAYSCALE)

#Mostramos la imagen a color y esto nos genera la ventana
cv2.imshow("ventana", img) 

#Generamos una ventana vacia para ahí mostrar las imagenes
# WINDOW_NORMAL permite redimencionar la ventana
# cv2.namedWindow("ventana",cv2.WINDOW_NORMAL)

# WINDOW_AUTOSIZE no nos permite modificar el tamaño de la ventana
# cv2.namedWindow("ventana",cv2.WINDOW_AUTOSIZE)

#Aplicamos la propiedad full screen a la ventana
cv2.namedWindow("ventana", cv2.WND_PROP_FULLSCREEN)

#Activamos la propiedad full screen en la ventana
cv2.setWindowProperty("ventana",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
# cv2.setWindowProperty("ventana",0,1)

while True:
    
    key = cv2.waitKey()
    
    if key == ord("4"):
        cv2.imshow("ventana", img)
    
    elif key == ord("6"):
        cv2.imshow("ventana", img2)
    else:
        break
    
cv2.destroyAllWindows()


