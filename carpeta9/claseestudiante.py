# Definimos la clase Estudiante con sus atributos y métodos
class Estudiante:
    # El constructor recibe el nombre, el apellido, el carnet y la carrera del estudiante
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera
    
    # El método cambiar_nombre recibe el nuevo nombre del estudiante y lo actualiza
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    # El método cambiar_apellido recibe el nuevo apellido del estudiante y lo actualiza
    def cambiar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido
    
    # El método cambiar_carnet recibe el nuevo carnet del estudiante y lo actualiza
    def cambiar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet
    
    # El método cambiar_carrera recibe la nueva carrera del estudiante y la actualiza
    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

# Creamos un objeto de la clase Estudiante con sus datos
estudiante = Estudiante("Pedro", "García", "PG1234", "Ingeniería Informática")

# Probamos los métodos para cambiar los atributos del estudiante
estudiante.cambiar_nombre("Pablo")
estudiante.cambiar_apellido("Gómez")
estudiante.cambiar_carnet("PG5678")
estudiante.cambiar_carrera("Matemáticas")
