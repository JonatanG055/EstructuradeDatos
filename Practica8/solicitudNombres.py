nombres = []

while True:
    nombre = input("Ingresa un nombre (o 'q' para salir): ")
    if nombre.lower() == 'q':
        break
    nombres.append(nombre)

with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")
