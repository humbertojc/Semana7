# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:47:35 2022

@author: user
"""

archivo = open("archivo_de_prueba.txt","wt")
contenido = "línea1 hola amigos ¿Cómo están?\nLínea2 Bienvenidos a la untels."
archivo.write(contenido)
archivo.close()