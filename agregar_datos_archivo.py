# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:57:29 2022

@author: user
"""

archivo = open("noticia.txt", "at")
# \n es para agregar el contenido en una linea final
contenido = "\nFuente: RPP"

archivo.write(contenido)
archivo.close()