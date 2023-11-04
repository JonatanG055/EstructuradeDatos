# main_geometria.py

import geometria

# Ejemplo de cálculo de área y perímetro
radio = 5
print(f"Área del círculo con radio {radio}: {geometria.calcular_area_circulo(radio)}")
print(f"Perímetro del círculo con radio {radio}: {geometria.calcular_perimetro_circulo(radio)}")

ancho = 4
largo = 6
print(f"Área del rectángulo de ancho {ancho} y largo {largo}: {geometria.calcular_area_rectangulo(ancho, largo)}")
print(f"Perímetro del rectángulo de ancho {ancho} y largo {largo}: {geometria.calcular_perimetro_rectangulo(ancho, largo)}")

base = 3
altura = 8
print(f"Área del triángulo con base {base} y altura {altura}: {geometria.calcular_area_triangulo(base, altura)}")
print(f"Perímetro del triángulo (no aplicable en un triángulo genérico)")
