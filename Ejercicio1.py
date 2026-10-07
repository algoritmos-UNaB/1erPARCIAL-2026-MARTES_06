class Pokemon:
    def __init__(self, nombre, tipo, nivel):
       self.nombre = nombre
       self.tipo = tipo
       self.nivel = nivel
    def subir_nivel (self):
        if self.nivel < 100:
            self.nivel += 1
    def __str__(self):
       return "Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"

class Entrenador:
    def __init__(self, nombre):
       self.nombre = nombre
       self.equipo = []
    def agregar_pokemon(self, nombre):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print("No se pueden tener mas de 6 Pokemon")
    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)
    def nivel_promedio(self):
        if len(self.equipo) == 0
           return: 0
        suma = 0
        for pokemon in self.equipo:
            suma += pokemon.nivel
        return suma / len()