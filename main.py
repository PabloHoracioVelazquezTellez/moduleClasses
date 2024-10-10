from mi_clase import Persona
from claseAlumno import Alumno

# Crear una instancia de la clase Persona
persona1 = Persona("Juan")

# Llamar al metodo saludar
print(persona1.saludar())

#Diccionario para almacenar a los 50 alumnos
registro_Alumnos = {}

for i in range(3):#Capturar registros
    alumno = Alumno()
    alumno.set_nombre(input(f"Ingrese el nombre del alumno {i+1}: "))
    alumno.set_apellido_paterno (input(f"Ingrese el apellido paterno del alumno {i+1}: "))
    alumno.set_apellido_materno (input(f"Ingrese el apellido materno del alumno {i+1}: "))
    alumno.set_no_control (input(f"Ingrese el número de control del alumno {i+1}: "))
    alumno.set_semestre (int(input(f"Ingrese el semestre del alumno {i+1}: ")))
    registro_Alumnos[i] = alumno

for i in range(3): #Mostrar registros
    print(f"Alumno: {registro_Alumnos[i].get_nombre()}")