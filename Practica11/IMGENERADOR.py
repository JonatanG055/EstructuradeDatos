import MODULO1GENNRADOR as generador  # Importa el módulo renombrado con un alias

# Ejemplo de generación de contraseñas
longitud_clave = 10
clave_generada = generador.generarclave(longitud_clave)  # Llama a la función generarclave
print(f"Contraseña generada: {clave_generada}")
