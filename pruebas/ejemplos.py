from cifrado.cesar import cifrado_cesar, descifrado_cesar
from cifrado.vigenere import cifrado_vigenere, descifrado_vigenere
from ataques.ataques import ataque_fuerza_bruta_cesar, ataque_diccionario_vigenere

def ejemplo_cifrado_cesar():
    texto = "La reconocida empresa Ciberpollo solicita apoyo"
    clave = 9
    print("\nEjemplo:\n")
    print("Mensaje a cifrar:", texto)
    print("Clave:", clave)
    print("Resultado:", cifrado_cesar(texto, clave))


def ejemplo_cifrado_vigenere():
    texto = "La reconocida empresa Ciberpollo solicita apoyo"
    clave = "iloveu"
    print("\nEjemplo:\n")
    print("Mensaje a cifrar:", texto)
    print("Clave:", clave)
    print("Resultado:", cifrado_vigenere(texto, clave))

def ejemplo_descifrado_cesar():
    texto_cifrado = cifrado_cesar("La reconocida empresa Ciberpollo solicita apoyo", 9)
    clave = 9
    print("\nEjemplo:\n")
    print("Mensaje cifrado:", texto_cifrado)
    print("Clave:", clave)
    print("Resultado:", descifrado_cesar(texto_cifrado, clave))

def ejemplo_descifrado_vigenere():
    texto_cifrado = cifrado_vigenere("La reconocida empresa Ciberpollo solicita apoyo", "iloveu")
    clave = "iloveu"
    print("\nEjemplo:\n")
    print("Mensaje cifrado:", texto_cifrado)
    print("Clave:", clave)
    print("Resultado:", descifrado_vigenere(texto_cifrado, clave))
