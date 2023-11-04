import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [12000, 15000, 18000, 14000, 16000]
}

# Crea un DataFrame con los datos
df = pd.DataFrame(data)

# Crea el gráfico de barras horizontales
plt.barh(df['Mes'], df['Ventas'])
plt.xlabel('Ventas')
plt.ylabel('Mes')
plt.title('Ventas Mensuales por Mes')

# Muestra el gráfico
plt.show()
