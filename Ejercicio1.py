class Pokemon:

    def __init__(self, nombre: str, tipo: str, nivel: int):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self, nivel):
        self.nivel < 100
        self.nivel + 1

    def __str__(self):
        return (f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}")

class Entrenador:

    def __init__(self, nameentrenador):
        self.nameentrenador = nameentrenador
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        if self.equipo >= 6:
            print("No se pueden agregar mas de 6 Pokemones.")
        else:
            self.equipo.append(pokemon)
    
    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio():
        if len(self.equipo) == 0:
            return 0

            contador = 0
        for pokemon in self.equipo:
            contador += pokemon.nivel
            
            return contador / len(self.equipo)

        