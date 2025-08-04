def cifrado_cesar(texto, clave):
    abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    resultado = ""

    texto = texto.upper()

    for letra in texto:
        if letra in abecedario:
            nueva_pos = (abecedario.index(letra) + clave) % len(abecedario)
            resultado += abecedario[nueva_pos]
        else:
            resultado += letra 

    return resultado

def descifrado_cesar(texto_cifrado, clave):
    abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    resultado = ""

    texto_cifrado = texto_cifrado.upper()

    for letra in texto_cifrado:
        if letra in abecedario:
            nueva_pos = (abecedario.index(letra) - clave) % len(abecedario)
            resultado += abecedario[nueva_pos]
        else:
            resultado += letra

    return resultado