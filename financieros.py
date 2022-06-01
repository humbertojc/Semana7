# -*- coding: utf-8 -*-
"""
Los módulos te permitirán crean librerías de funcionalidades que 
puedes utilizar o reutilizar en cualquier momento.
"""
igv = 0.18

def obtenerIGVsubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal*(1+0.18)
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)
