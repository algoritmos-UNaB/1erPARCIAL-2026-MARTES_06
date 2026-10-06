class pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int):
        self.nombre: str = nombre
        self.tipo: str = tipo
        if nivel < 1:
            self.nivel: int = 1
        elif nivel > 100:
            self.nivel: int = 100
        else:
            self.nivel: int = nivel
    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"

class Entrenador:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.equipo: list = []
    def agregar_pokemon(self, pokemon: Pokemon):
        if len(self.equipo) >= 6:
            print("El equipo esta lleno. No se pueden tener mas de 6 pokemon")
        else:
            self.equipo.append(pokemon)
    def mostrar_equipo(self):
        if not self.equipo:
            print(f"El equipo de {self.nombre} esta vacio.")
        else:
            print(f"Equipo de {self.nombre}:")
            for pokemon in self.equipo:
                print(f"- {pokemon}")
    def nivel_promedio(self) -> float:
        if not self.equipo:
            return 0.0
        suma_niveles = sum(pokemon.nivel for pokemon in self.equipo)
        return suma_niveles / Len(self.equipo)

    
