class Persona():
    def __init__(self, nombre, edad, profesion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def saludar(self):
        print("Hola")
    def despedirse(self):
        print("Chao")

persona_1 = Persona("Hector", 36, "IngenieroSistemas")
print(persona_1.nombre)
persona_1.saludar()