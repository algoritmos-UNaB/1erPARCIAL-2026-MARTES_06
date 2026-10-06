#Ejercicio 1: Implementación de TADs

class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
        else: 
            print("El Pokémon ya está al máximo nivel")

    def __str__(self): 
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"

class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print("No se pueden agregar más Pokémon")

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        if len(self.equipo) > 0:
            total_niveles = sum(pokemon.nivel for pokemon in self.equipo)
            return total_niveles / len(self.equipo)
        else:
            return 0
        