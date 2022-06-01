# Dado el subtotal, calcular el igv y el total

import financieros
subtotal = 800.77
print(f"subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVsubtotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal): .2f}")