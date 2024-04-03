def espiral(fila, columna):

    if fila >= columna: 
        if fila % 2 == 1: # los numeros aumentan hacia la derecha si son impares
            return fila ** 2 - columna + 1 
        else: # si es par aumenta hacia la izquierda
            return (fila - 1) ** 2 + columna
    else:
        if columna % 2 == 0: # aumenta hacia abajo
            return columna ** 2 - fila + 1
        else: # aumenta hacia arriba
            return (columna - 1) ** 2 + fila


fila = int(input('Ingrese la fila a la que quiere acceder: '))
columna = int(input('Ingrese la columna a la que quiere acceder: '))
print(espiral(columna, fila))

assert espiral(2, 2) == 3, "Error en el caso de prueba"
print('Todos los casos de prueba han pasado correctamente.')