# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:36:56 2022

@author: user
"""
# Importamos la libreria
import camelcase
# Tenemos una cadena llamada nombre y se desea que se muestre el formato
# titulo
nombre = "humberto julca espillco"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam

cam = camelcase.CamelCase()

print("Con Calmelcase....")

# Imprimimos el nombre en formato titulo
# Utilizamos camelcase

print(cam.hump(nombre))

# Para resolver el problema creamos otro objeto cam2
# Al definir el obejeto, incluimos los argumentos 'humberto' y 'espillco'

cam2 = camelcase.CamelCase('humberto', 'espillco')

print(cam2.hump(nombre))