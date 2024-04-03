# def palindromo(txt: str):
#     txt = txt.replace(' ','').lower()
#     return txt == txt[::-1]

# text_1 = 'ana'

# print(palindromo(text_1))

def palindromo(txt: str):
    # Contamos las letras que se repiten
    contador = {} 
    for letra in txt:
        # Si ya hay una letra repetida se le suma 1
        if letra in contador:
            contador[letra] += 1
        else: # si no, significa que solo hay una
            contador[letra] = 1
    # verificamos cuantas letras impares hay
    #                    la letra, la cantidad de veces que se repite
    impares = [letra for letra, frecuencia in contador.items() if frecuencia % 2 == 1]
    # si hay mas de 1, entonces no se puede formar un palindromo
    if len(impares) > 1:
        return "NO SOLUTION"
    
    if len(impares) == 0: # si no hay letras impares va a estar vacío
        medio = ''
    else: 
        medio = impares[0] # si hay impares, va a tomar el primero de la lista
    # Construimos la parte izquierda del palíndromo
    izquierda = ''
    for letra, frecuencia in contador.items():
        # Lo que hace este bucle es ir agregando las letras del lado izquierdo
        izquierda += letra * (frecuencia // 2)
    
    # La parte derecha es la copia de la parte izquierda pero invertida
    derecha = izquierda[::-1]

    # retornamos el palindromo completo
    return izquierda + medio + derecha

texto = "aabbb"
resultado = palindromo(texto.lower()) # si no usaramos el metodo .lower() entonces en el ejemplo 
# podria formar un palindromo, ya que a B lo contaria como una letra diferente a b
print(resultado)


assert palindromo("aabbc") == "abcba", "Error en el caso de prueba"
print('Todos los casos de prueba han pasado correctamente.')