# ataques.py
from cifrado.cesar  import descifrado_cesar
from cifrado.vigenere import descifrado_vigenere

def ataque_fuerza_bruta_cesar(texto):
    print("\nPosibles claves (César):")
    for k in range(27):
        print(f"Clave {k:2d}: {descifrado_cesar(texto, k)}")

def ataque_diccionario_vigenere(texto, ruta_diccionario="rockyou-top100.txt"):
    print("\nProbando claves del diccionario...")
    try:
        with open(ruta_diccionario, encoding="utf-8") as f:
            claves = [line.strip() for line in f]
    except FileNotFoundError:
        print("Archivo de diccionario no encontrado.")
        return
    for clave in claves:
        posible = descifrado_vigenere(texto, clave)
        print(f"[{clave}] → {posible}")