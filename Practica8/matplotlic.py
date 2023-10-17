import matplotlib.pyplot as plt
# Datos de ejemplo
x = ["A", "B", "C", "D"]
y = [10, 15, 12, 8]
# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar las barras
ax.bar(x, y)
# Añadir título y etiquetas
ax.set_title("Gráfico de barras")
ax.set_xlabel("Categorías")
ax.set_ylabel("Valores")
# Mostrar el gráfico
plt.show()
