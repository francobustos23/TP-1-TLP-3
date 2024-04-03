# def palindromo(txt: str):
#     txt = txt.replace(' ','').lower()
#     return txt == txt[::-1]

# text_1 = 'ana'

# print(palindromo(text_1))

def palindromo(txt: str):
    # Contamos las ocurrencias de cada letra en el texto manualmente
    contador = {}
    for letra in txt:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

    impares = [letra for letra, frecuencia in contador.items() if frecuencia % 2 == 1]
    if len(impares) > 1:
        return "NO SOLUTION"

    medio = '' if len(impares) == 0 else impares[0]
    
    # Construimos la parte izquierda del palíndromo
    izquierda = ''
    for letra, frecuencia in contador.items():
        izquierda += letra * (frecuencia // 2)
    
    # La parte derecha es simplemente la parte izquierda invertida
    derecha = izquierda[::-1]

    return izquierda + medio + derecha

texto = "aabcbbB"
resultado = palindromo(texto.lower())
print(resultado)


assert palindromo("aabbc") == "abcba", "Error en el caso de prueba"
print('Todos los casos de prueba han pasado correctamente.')