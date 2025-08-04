def cifrado_vigenere(texto, clave):
    abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    resultado = ""
    texto = texto.upper()
    clave = clave.upper()
    clave_expandida = ""
    indice = 0

    for letra in texto:
        if letra in abecedario:
            clave_expandida += clave[indice % len(clave)]
            indice += 1
        else:
            clave_expandida += letra

    for i in range(len(texto)):
        if texto[i] in abecedario:
            pos = (abecedario.index(texto[i]) + abecedario.index(clave_expandida[i])) % len(abecedario)
            resultado += abecedario[pos]
        else:
            resultado += texto[i]

    return resultado

def descifrado_vigenere(texto_cifrado, clave):
    abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    resultado = ""
    texto_cifrado = texto_cifrado.upper()
    clave = clave.upper()
    clave_expandida = ""
    indice = 0

    for letra in texto_cifrado:
        if letra in abecedario:
            clave_expandida += clave[indice % len(clave)]
            indice += 1
        else:
            clave_expandida += letra

    for i in range(len(texto_cifrado)):
        if texto_cifrado[i] in abecedario:
            pos = (abecedario.index(texto_cifrado[i]) - abecedario.index(clave_expandida[i])) % len(abecedario)
            resultado += abecedario[pos]
        else:
            resultado += texto_cifrado[i]

    return resultado
