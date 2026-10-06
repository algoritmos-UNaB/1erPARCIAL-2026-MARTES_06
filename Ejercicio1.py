class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int = 1):
        self.nombre = nombre
        self.tipo = tipo
        if 1 <= nivel <= 100:
            self.nivel = nivel
        else:
            self.nivel = 1

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
        else:
            print(f"{self.nombre} ya esta en el nivel maximo (100).")

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
            print("No se pueden tener mas Pokemon en el equipo.")

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(str(pokemon))

    def nivel_promedio(self):
        if len(self.equipo) == 0:
            return 0
        
        suma = 0
        for pokemon in self.equipo:
            suma += pokemon.nivel
            
        return suma / len(self.equipo)