def encontrar_numero(cantidad, numeros):
    # Esta es una formula de saber la suma de todos los numeros de la cantidad total
    suma_cantidad = (cantidad * (cantidad + 1)) // 2
    # Hacemos la suma de los numeros de la lista
    sum_numeros = sum(numeros)
    # Con la cantidad total y la suma de los numeros de la lista
    numero_faltante = suma_cantidad - sum_numeros
    # Obtenemos el numero faltante y lo retornamos
    return numero_faltante

assert encontrar_numero(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
print(encontrar_numero(5, [1,2,4,5]))
print('Todos los casos de prueba han pasado correctamente.')