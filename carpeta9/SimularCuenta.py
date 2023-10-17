# Definimos una excepción personalizada para indicar que el usuario o la contraseña son incorrectos
class CredencialesInvalidas(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

# Definimos la clase Usuario con sus atributos y métodos
class Usuario:
    # El constructor recibe el nombre de usuario y la contraseña
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    # El método login recibe el nombre de usuario y la contraseña que se intentan usar para acceder
    def login(self, username, password):
        # Comprobamos si el nombre de usuario y la contraseña coinciden con los del objeto
        if username == self.username and password == self.password:
            return True  # Si coinciden, devuelve True
        else:
            raise CredencialesInvalidas("El usuario o la contraseña son incorrectos")  # Si no coinciden, lanza una excepción

# Creamos un objeto de la clase Usuario con sus datos
usuario = Usuario("juan", "1234")

# Probamos el método login con diferentes credenciales
if usuario.login("juan", "1234"):
    print("Acceso concedido")  # Si el login es exitoso, se muestra este mensaje
else:
    print("Acceso denegado")  # Si el login falla, se muestra este mensaje

try:
    usuario.login("ana", "5678")  # Intentamos acceder con credenciales incorrectas, lo que lanzará una excepción
except CredencialesInvalidas as e:
    print(e.mensaje)  # Imprimimos el mensaje de la excepción
