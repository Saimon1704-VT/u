def sumaArreglo(arreglo):
    if not arreglo:
        return 0
    else:
        return arreglo[0] + sumaArreglo(arreglo[1:])

mi_arreglo = [1, 2, 3, 4, 5]
resultado = sumaArreglo(mi_arreglo)
print("La suma es:", resultado)
