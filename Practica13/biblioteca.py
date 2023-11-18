class Biblioteca:
    def __init__(self):
        self.pila = []

    def prestar(self, libro):
        if libro not in self.pila:
            self.pila.append(libro)
            print(f"Se ha prestado {libro}.")
        else:
            print(f"El libro {libro} ya está prestado.")

    def devolver(self, libro):
        if libro in self.pila:
            self.pila.remove(libro)
            print(f"Se ha devuelto {libro}.")
        else:
            print(f"No se encuentra el libro {libro} prestado.")

    def mostrar_estado(self):
        print(f"Estado de la pila: {self.pila}")