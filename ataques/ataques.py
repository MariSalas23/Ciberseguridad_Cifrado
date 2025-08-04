from cifrado.cesar  import descifrado_cesar
from cifrado.vigenere import descifrado_vigenere
from recursos.rockyou_top100 import passwords

def ataque_fuerza_bruta_cesar(texto):
    print("\nPosibles claves (César):")
    for k in range(27):
        print(f"Clave {k:2d}: {descifrado_cesar(texto, k)}")

def ataque_diccionario_vigenere(texto):
    print("\nProbando claves del diccionario...\n")
    for clave in passwords:
        posible = descifrado_vigenere(texto, clave)
        print(f"{clave}: {posible}")