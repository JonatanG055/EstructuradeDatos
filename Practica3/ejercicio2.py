# Solicitar al usuario que ingrese una cadena
cadena = input("Ingrese una cadena de texto: ")

# Convertir la cadena en una lista de palabras
palabras = cadena.split()

# Contar la cantidad de palabras en la lista
cantidad_palabras = len(palabras)

# Mostrar el número de palabras
print(f"La cadena tiene {cantidad_palabras} palabras.")
