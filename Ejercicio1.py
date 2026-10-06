# Ejercicio 1: TADs (Pokemon y Entrenador)

class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel    # entre 1 y 100

    def subir_nivel(self):
        # Sólo sube si todavía no llegó al máximo
        if self.nivel < 100:
            self.nivel += 1

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"  # respetando el formato del enunciado

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []    # lista vacía de Pokemon

    def agregar_pokemon(self, pokemon):
        if len(self.equipo) >= 6:
            print("No se pueden tener más de 6 Pokémon en el equipo.")
        else:
            self.equipo.append(pokemon)

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)   # print llama a __str__ automáticamente

    def nivel_promedio(self):
        if len(self.equipo) == 0:  # equipo vacío (caso especial)
            return 0
        total = 0
        for pokemon in self.equipo:
            total += pokemon.nivel
        return total / len(self.equipo)
