# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:33:03 2022

@author: user
"""

noticia = open("noticia.txt", "rt", encoding='utf8')

datos_noticia = noticia.read()

print(datos_noticia)