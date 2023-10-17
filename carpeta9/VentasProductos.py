# Definimos una excepción personalizada para indicar que no hay suficiente stock
class StockInsuficiente(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

# Definimos la clase Articulo con sus atributos y métodos
class Articulo:
    # El constructor recibe el nombre, la cantidad y el precio del artículo
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    # El método vender recibe la cantidad de unidades que se quieren vender
    def vender(self, unidades):
        # Si hay suficiente stock, se realiza la venta y se actualiza la cantidad
        if unidades <= self.cantidad:
            self.cantidad -= unidades
            print(f"Se han vendido {unidades} unidades de {self.nombre}")
            print(f"El total a pagar es {unidades * self.precio} euros")
        # Si no hay suficiente stock, se lanza una excepción personalizada
        else:
            raise StockInsuficiente(f"No hay suficientes unidades de {self.nombre}")

# Creamos un objeto de la clase Articulo con sus datos
articulo = Articulo("Lápiz", 10, 0.5)

# Probamos el método vender con diferentes cantidades
articulo.vender(5) # Se venden 5 unidades
try:
    articulo.vender(6) # Intentamos vender 6 unidades, pero lanzará una excepción StockInsuficiente
except StockInsuficiente as e:
    print(e.mensaje)  # Imprimirá el mensaje de la excepción
