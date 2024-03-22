"""
Considera un algoritmo que toma como entrada un entero positivo n. Si n es par, el algoritmo
lo divide por dos, y si n es impar, el algoritmo lo multiplica por tres y le suma uno. El
algoritmo repite esto hasta que n sea uno. Por ejemplo, la secuencia para el valor 3 es la
siguiente:
3 ➝ 10 ➝ 5 ➝ 16 ➝ 8 ➝ 4 ➝ 2 ➝ 1

Tu tarea es simular la ejecución del algoritmo para un valor dado de n.
Input:
La única línea de entrada contiene un entero n.
Output:
Imprime una línea que contenga todos los valores de n durante la ejecución del algoritmo.
Constraints:
1 < n < 10^6
"""
numero = int(input('Ingresa el numero crack: '))
def calcular_secuencia(numero):
    secuencia = [numero]
    while numero > 1:
        if numero % 2 == 0:
            #si el numero es par
            numero //= 2 #lo divide por dos sin residuo
        else:
            #si es impar
            numero = numero * 3 + 1 #lo multiplica y le suma 1
        secuencia.append(numero) # es como el push de js, agrega un elemento al final de la lista
    return secuencia #devuelve la lista de los elementos 

print(calcular_secuencia(numero)) #pasamos como argumento el valor que ingreso el usuario
assert calcular_secuencia(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"


