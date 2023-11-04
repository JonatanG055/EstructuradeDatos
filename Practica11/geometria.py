

import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def calcular_area_rectangulo(ancho, largo):
    return ancho * largo

def calcular_perimetro_rectangulo(ancho, largo):
    return 2 * (ancho + largo)

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3
