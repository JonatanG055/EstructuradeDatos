try:
    with open("archivo.txt", "r") as archivo:
        for linea in archivo:
            print(linea, end="")
except FileNotFoundError:
    print("El archivo 'archivo.txt' no se encontró.")
