import matplotlib.pyplot as plt
# Datos de ejemplo
x = ["A", "B", "C", "D"]
y = [25, 35, 15, 25]
# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar el gráfico circular
ax.pie(y, labels=x)
# Añadir título
ax.set_title("Gráfico circular")
# Mostrar el gráfico
plt.show()

