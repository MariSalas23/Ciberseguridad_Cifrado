# main.py
from cifrado.cesar import cifrado_cesar, descifrado_cesar
from cifrado.vigenere import cifrado_vigenere, descifrado_vigenere
from ataques.ataques import ataque_fuerza_bruta_cesar, ataque_diccionario_vigenere
from clave.clave import pedir_clave_cesar, pedir_clave_vigenere

def menu():
    while True:
        print("\nMENÚ:\n")
        print("1. Cifrado César")
        print("2. Descifrado César")
        print("3. Cifrado Vigenère")
        print("4. Descifrado Vigenère")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")
        print("")

        if opcion == "1":
            texto = input("Mensaje a cifrar: ")
            clave = pedir_clave_cesar()
            print("\nResultado:", cifrado_cesar(texto, clave))

        elif opcion == "2":
            texto = input("Mensaje cifrado: ")
            tiene_clave = input("¿Tiene la clave? (s/n): ").strip().lower()
            if tiene_clave == "s":
                clave = pedir_clave_cesar()
                print("\nResultado:", descifrado_cesar(texto, clave))
            else:
                print("\nIniciando ataque por fuerza bruta...")
                ataque_fuerza_bruta_cesar(texto)

        elif opcion == "3":
            texto = input("Mensaje a cifrar: ")
            clave = pedir_clave_vigenere()
            print("\nResultado:", cifrado_vigenere(texto, clave))

        elif opcion == "4":
            texto = input("Mensaje cifrado: ")
            tiene_clave = input("¿Tiene la clave? (s/n): ").strip().lower()
            if tiene_clave == "s":
                clave = pedir_clave_vigenere()
                print("\nResultado:", descifrado_vigenere(texto, clave))
            else:
                print("\nIniciando ataque con diccionario...")
                ataque_diccionario_vigenere(texto)

        elif opcion == "0":
            print("\n¡Gracias por escoger a Firewallín!")
            break

        else:
            print("\nOpción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
