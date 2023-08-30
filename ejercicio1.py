# Definir una tupla con los meses del año
meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

# Solicitar al usuario que ingrese un número entre 1 y 12
numero = int(input("Ingrese un número entre 1 y 12: "))

# Verificar si el número está dentro del rango válido
if numero >= 1 and numero <= 12:
    # Mostrar el mes correspondiente al número ingresado
    print(f"El mes es {meses[numero - 1]}")
else:
    # Mostrar un mensaje de error si el número está fuera de rango
    print("Número fuera de rango. Por favor, ingrese un número entre 1 y 12.")
