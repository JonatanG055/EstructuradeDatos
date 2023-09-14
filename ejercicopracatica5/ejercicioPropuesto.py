# Función para calcular la suma de números indeterminados
def suma(*args):
    return sum(args)

# Función para calcular la raíz n de un número
def raiz_n(numero, n):
    if numero < 0 and n % 2 == 0:
        raise ValueError("No se puede calcular la raíz n de un número negativo con un exponente par.")
    return numero ** (1/n)

# Función para realizar la división con manejo de división por cero
def division(dividendo, divisor):
    if divisor == 0:
        return "La división entre cero no está definida."
    else:
        return dividendo / divisor

# Funciones para operaciones con listas
def ingresar_datos_lista(n):
    datos = []
    for _ in range(n):
        dato = float(input("Ingrese un dato: "))
        datos.append(dato)
    return datos

def ordenar_lista(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def sumatoria_lista(lista):
    total = 0
    for dato in lista:
        total += dato
    return total

def media_lista(lista):
    total = sumatoria_lista(lista)
    n = len(lista)
    if n > 0:
        return total / n
    else:
        return 0

def mediana_lista(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        medio1 = lista_ordenada[n // 2 - 1]
        medio2 = lista_ordenada[n // 2]
        return (medio1 + medio2) / 2

def moda_lista(lista):
    contador = {}
    for dato in lista:
        if dato in contador:
            contador[dato] += 1
        else:
            contador[dato] = 1

    moda = max(contador, key=contador.get)
    return moda

def desviacion_estandar(lista):
    media = media_lista(lista)
    n = len(lista)
    suma_cuadrados = sum((dato - media) ** 2 for dato in lista)
    desviacion = (suma_cuadrados / n) ** 0.5
    return desviacion

# Ejemplo de uso:
if __name__ == "__main__":
    numeros = [3, 6, 9, 12]
    resultado_suma = suma(*numeros)
    print("Resultado de la suma:", resultado_suma)

    numero = 16
    n = 4
    resultado_raiz = raiz_n(numero, n)
    print(f"Raíz {n}-ésima de {numero}: {resultado_raiz}")

    dividendo = 10
    divisor = 0
    resultado_division = division(dividendo, divisor)
    print("Resultado de la división:", resultado_division)

    n = 5
    datos = ingresar_datos_lista(n)
    print("Lista de datos ingresados:", datos)

    ordenar_lista(datos)
    print("Lista ordenada de menor a mayor:", datos)

    suma_total = sumatoria_lista(datos)
    print("Sumatoria de datos:", suma_total)

    media = media_lista(datos)
    print("Media de datos:", media)

    mediana = mediana_lista(datos)
    print("Mediana de datos:", mediana)

    moda = moda_lista(datos)
    print("Moda de datos:", moda)

    desviacion = desviacion_estandar(datos)
    print("Desviación estándar de datos:", desviacion)
