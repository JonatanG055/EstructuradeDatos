import matplotlib.pyplot as plt
# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar los puntos
ax.scatter(x, y)
# Añadir título y etiquetas
ax.set_title("Gráfico de dispersión")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
# Mostrar el gráfico
plt.show()
