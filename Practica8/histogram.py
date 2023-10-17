import matplotlib.pyplot as plt
# Datos de ejemplo
x = [1.2, 2.3, 3.1, 4.5,
     2.1, 3.4, 1.8, 3.9,
     4.2, 3.7, 2.6, 4.1]
# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar el histograma
ax.hist(x)
# Añadir título y etiquetas
ax.set_title("Histograma")
ax.set_xlabel("Valores")
ax.set_ylabel("Frecuencia")
# Mostrar el gráfico
plt.show()

