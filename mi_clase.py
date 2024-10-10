# mi_clase.py
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def saludar(self):
        return f"Hola {self.__nombre}."
