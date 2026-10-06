# Ejercicio 1: Implementación de TADs

class Pokemon:

    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel = self.nivel + 1
    
    def __str__(self):
        return f "Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"

class Entrenador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        if len(self.equipo) >= 6:
            print("No se pueden tener más de 6 Pokémon.")
        else:
            self.equipo.append(pokemon)
    
    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        if len(self.equipo) == 0:
            return 0
        
        suma_nivel = 0

        for pokemon in self.equipo:
            suma_nivel = suma_nivel + pokemon.nivel

        return suma_nivel/len(self.equipo)