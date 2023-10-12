try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró. Verifique la ruta o cree el archivo si no existe.")
