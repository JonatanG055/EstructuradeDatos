class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, cliente):
        self.items.append(cliente)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def __str__(self):
        return f"{self.items}"


def atender_clientes(cola, biblioteca):
    while not cola.esta_vacia():
        cliente = cola.desencolar()
        libro = input(f"{cliente}, ¿qué libro desea prestar? ")
        if libro:
            biblioteca.prestar(libro)
            print(f"{cliente} ha sido atendido. Estos son los libros prestados: {biblioteca.pila}")


def main():
    from biblioteca import Biblioteca  # Importa la clase Biblioteca del módulo biblioteca
    biblioteca = Biblioteca()
    cola = Cola()

    while True:
        print("\nMenú:")
        print("1. Prestar libro")
        print("2. Devolver libro")
        print("3. Atender clientes")
        print("4. Salir")

        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            libro = input("Ingrese el título del libro a prestar: ")
            biblioteca.prestar(libro)
        elif opcion == 2:
            libro = input("Ingrese el título del libro a devolver: ")
            biblioteca.devolver(libro)
        elif opcion == 3:
            cliente = input("Ingrese el nombre del cliente: ")
            cola.encolar(cliente)
        elif opcion == 4:
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

        biblioteca.mostrar_estado()

    atender_clientes(cola, biblioteca)


if __name__ == "__main__":
    main()
