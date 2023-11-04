import random
import string

def generarclave(longitud):
    caracteres = string.ascii_letters + string.digits  # Letras mayúsculas, minúsculas y números
    clave = ''.join(random.choice(caracteres) for _ in range(longitud))
    return clave
