class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int = 1):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = max(1, min(100, nivel))

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"


class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon: Pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print("El equipo ya está completo (máximo 6 Pokémon).")

    def mostrar_equipo(self):
        if not self.equipo:
            print(f"El equipo de {self.nombre} está vacío.")
            return

        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self) -> float:
        if not self.equipo:
            return 0.0

        suma_niveles = sum(pokemon.nivel for pokemon in self.equipo)
        return suma_niveles / len(self.equipo)
    