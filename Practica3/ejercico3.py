# Inicializar una lista vacía para almacenar las notas
notas = []

# Solicitar al usuario que ingrese las 5 notas
for i in range(5):
    nota = float(input(f"Ingrese la nota {i + 1} (entre 0 y 10): "))
    # Verificar si la nota está en el rango válido
    if nota >= 0 and nota <= 10:
        notas.append(nota)
    else:
        print("Nota fuera de rango. Por favor, ingrese una nota entre 0 y 10.")

# Mostrar todas las notas
print("Notas obtenidas:", notas)

# Calcular la nota media
nota_media = sum(notas) / len(notas)
print("Nota media:", nota_media)

# Calcular la nota más alta y la menor
nota_maxima = max(notas)
nota_minima = min(notas)
print("Nota más alta:", nota_maxima)
print("Nota menor:", nota_minima)
