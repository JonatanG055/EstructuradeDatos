# Crear un diccionario con nombres y precios de productos
productos = {
    "producto1": 10.0,
    "producto2": 20.0,
    "producto3": 15.0,
    "producto4": 25.0,
}

def calcular_total(producto, cantidad):
    if producto in productos:
        precio_unitario = productos[producto]
        total = precio_unitario * cantidad
        return total
    else:
        return None

def main():
    producto = input("Ingrese el nombre del producto: ").lower()  # Convertir a minúsculas para evitar errores de mayúsculas/minúsculas
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))

    total = calcular_total(producto, cantidad)

    if total is not None:
        print(f"Total a pagar por {cantidad} {producto}: ${total:.2f}")
    else:
        print(f"El producto '{producto}' no se encuentra disponible.")

if __name__ == "__main__":
    main()
