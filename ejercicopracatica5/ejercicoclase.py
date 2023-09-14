# Función para mostrar la lista
def mostrar_lista(lista):
    print("Lista actual:", lista)

# Función para agregar un elemento a la lista
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    print(f"Elemento '{elemento}' agregado a la lista.")

# Función para modificar un elemento en la lista
def modificar_elemento(lista, indice, nuevo_elemento):
    if indice >= 0 and indice < len(lista):
        lista[indice] = nuevo_elemento
        print(f"Elemento en el índice {indice} modificado a '{nuevo_elemento}'.")
    else:
        print("Índice fuera de rango. No se puede modificar el elemento.")

# Función para eliminar un elemento de la lista
def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
        print(f"Elemento '{elemento}' eliminado de la lista.")
    else:
        print(f"Elemento '{elemento}' no encontrado en la lista. No se puede eliminar.")

# Lista inicial
mi_lista = [1, 2, 3, 4, 5]

while True:
    print("\nOpciones:")
    print("1. Mostrar lista")
    print("2. Agregar elemento")
    print("3. Modificar elemento")
    print("4. Eliminar elemento")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        mostrar_lista(mi_lista)
    elif opcion == '2':
        elemento = input("Ingresa el elemento que deseas agregar: ")
        agregar_elemento(mi_lista, elemento)
    elif opcion == '3':
        indice = int(input("Ingresa el índice del elemento que deseas modificar: "))
        nuevo_elemento = input("Ingresa el nuevo elemento: ")
        modificar_elemento(mi_lista, indice, nuevo_elemento)
    elif opcion == '4':
        elemento = input("Ingresa el elemento que deseas eliminar: ")
        eliminar_elemento(mi_lista, elemento)
    elif opcion == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
