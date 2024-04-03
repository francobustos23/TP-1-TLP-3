numero = int(input('Ingrese un numero entero positivo: '))

def funcion_algoritmo(n):
    # agregamos el primer valor que es n
    secuen = [n]
    # restricciones
    if 1 < n < 10**6:
        # mientras n sea distinto a 1
        while n != 1:
            if n % 2 == 0: # si es par
                n = n // 2
            else: # si es impar
                n = n * 3 + 1
            secuen.append(n) # agrega el valor de n modificado 
    return secuen  # retorna la lista 

print(funcion_algoritmo(numero))

assert funcion_algoritmo(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print('Todos los casos de prueba han pasado correctamente. 😎')
