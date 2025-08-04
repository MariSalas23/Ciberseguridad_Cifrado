def pedir_clave_cesar():
    while True:
        try:
            return int(input("Ingrese clave numérica: "))
        except ValueError:
            print("La clave debe ser un número entero.")

def pedir_clave_vigenere():
    while True:
        clave = input("Ingrese clave de palabra: ").strip()
        if clave.isalpha():
            return clave
        else:
            print("La clave debe contener solo letras.")