def ingresar_notas_estudiantes(n):
    estudiantes = {}
    
    for i in range(n):
        nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
        nota1 = float(input(f"Ingrese la nota 1 del estudiante {nombre}: "))
        nota2 = float(input(f"Ingrese la nota 2 del estudiante {nombre}: "))
        nota3 = float(input(f"Ingrese la nota 3 del estudiante {nombre}: "))
        
        # Calcula el promedio de las notas
        promedio = (nota1 + nota2 + nota3) / 3
        
        estudiantes[nombre] = {
            'Nota 1': nota1,
            'Nota 2': nota2,
            'Nota 3': nota3,
            'Promedio': promedio
        }
    
    return estudiantes

def mostrar_tabla_estudiantes(estudiantes):
    print("\nTabla de Estudiantes y Notas:")
    print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Nombre", "Nota 1", "Nota 2", "Nota 3", "Promedio"))
    
    for nombre, notas in estudiantes.items():
        print("{:<15} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f}".format(nombre, notas['Nota 1'], notas['Nota 2'], notas['Nota 3'], notas['Promedio']))

def main():
    n = int(input("Ingrese la cantidad de estudiantes: "))
    estudiantes = ingresar_notas_estudiantes(n)
    mostrar_tabla_estudiantes(estudiantes)

if __name__ == "__main__":
    main()
