class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int = 1)
        if not 1 <= nivel <= 100:
                raise ValueError("El nivel debe estar entre 1 y 100")
            self.nombre = nombre
            self.tipo = tipo
            self.nivel = nivel

    def subir_nivel(self):
        if self.nivel < 100:
        self.nivel += 1
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"

class Entrenador:
    MAX_EQUIPO = 6

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = []
    
    def agregar_pokemon(self, pokemon: Pokemon):
        if len(self.equipo) >= self.MAX_EQUIPO:
            print("No se pueden tener más de 6 pokémon en el equipo")
        else
            self.equipo.append(pokemon)

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        if not self.equipo:
            return 0
        return sum(p.nivel for p in self.equipo) / len(self.equipo)

if __name__ == "__main__":
    ash = Entrenador("Ash")
    ash.agregar_pokemon(Pokemon("Pikachu", "Electrico", 25))
    ash.agregar_pokemon(Pokemon("Charmander", "Fuego", 10))
    ash.equipo[0].subir_nivel()
    ash.mostrar_equipo()
    print("nivel promedio", ash.nivel_promedio())
    for i in range(5):
        ash.agregar_pokemon(Pokemon(f"Estra{i}", "Agua", 5))