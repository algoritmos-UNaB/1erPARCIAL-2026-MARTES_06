class Pokemmon:
    def__init__(self, nombre: str, tipo: str, nivel: int):
        self.nombre = nombre
        self.tipo
# nivel inicial dentro del rango permitido
        self.nivel = max(1, min(nivel, 100))

    def subir_nivel(self)
        if self.nivel < 100
            self.nivel +1

    def__str__(self)
       
        return f "Nombre:{self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"


class Entrenador:
    def__init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = []

    def agregar_poquemon(sel, poquemon: Pokemmon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)

        else:
            print("No se pueden tener mas Pokemon en este equipo (max 6). ")

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(poquemon)  

     def nivel_promedio(self) -> float:
        if not self.equipo:
            return 0.0

        total_niveles = sum(pokemon.nivel for pokemon in self.equipo)
        return total_niveles / len(self.equipo)

        