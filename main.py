from cifrado.cesar import cifrado_cesar, descifrado_cesar
from cifrado.vigenere import cifrado_vigenere, descifrado_vigenere
from ataques.ataques import ataque_fuerza_bruta_cesar, ataque_diccionario_vigenere
from clave.clave import pedir_clave_cesar, pedir_clave_vigenere

def menu():
    while True:
        print("\nMENÚ:\n")
        print("1. Cifrado")
        print("2. Descifrado")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")
        print("")

        if opcion == "1":
            print("\n---- CIFRADO ----")
            print("1. Cifrado César")
            print("2. Cifrado Vigenère")
            subopcion = input("\nSeleccione tipo de cifrado: ")

            if subopcion == "1":
                texto = input("\nMensaje a cifrar: ")
                clave = pedir_clave_cesar()
                print("\nResultado:", cifrado_cesar(texto, clave))

            elif subopcion == "2":
                texto = input("\nMensaje a cifrar: ")
                clave = pedir_clave_vigenere()
                print("\nResultado:", cifrado_vigenere(texto, clave))

            else:
                print("\nOpción inválida. Intente de nuevo.")

        elif opcion == "2":
            print("\n----- DESCRIFRADO -----")
            print("1. Descifrado César")
            print("2. Descifrado Vigenère")
            subopcion = input("\nSeleccione tipo de descifrado: ")

            if subopcion == "1":
                texto = input("\nMensaje cifrado: ")
                tiene_clave = input("¿Tiene la clave? (s/n): ").strip()
                if tiene_clave == "s":
                    clave = pedir_clave_cesar()
                    print("\nResultado:", descifrado_cesar(texto, clave))
                elif tiene_clave == "n":
                    print("\nIniciando ataque por fuerza bruta...")
                    ataque_fuerza_bruta_cesar(texto)
                else:
                    print("\nOpción inválida. Intenta de nuevo.")

            elif subopcion == "2":
                texto = input("\nMensaje cifrado: ")
                tiene_clave = input("¿Tiene la clave? (s/n): ").strip()
                if tiene_clave == "s":
                    clave = pedir_clave_vigenere()
                    print("\nResultado:", descifrado_vigenere(texto, clave))
                elif tiene_clave == "n":
                    print("\nIniciando ataque con diccionario...")
                    ataque_diccionario_vigenere(texto)
                else:
                    print("\nOpción inválida. Intenta de nuevo.")

            else:
                print("\nOpción inválida. Intenta de nuevo.")

        elif opcion == "0":
            print("\n¡Gracias por escoger a Firewallín!")
            break

        else:
            print("\nOpción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
