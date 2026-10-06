class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int):
        if not isinstance (nombre, str) or not isinstance (tipo, str):
            raise TypeError('Nombre y/o tipo debe ser texto')
        if not isinstance (nivel, int) or not (1 <= nivel <=100):
            raise ValueError('Elije entre el nivel 1 y el 100')
        self.nombre = nombre
        self.tipo = tipo 
        self.nivel = nivel

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
        else:
            print('Nivel maximo alcanzado!')


    def __str__(self):
        return f'Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}'

class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        if len(self.equipo) >= 6:
            print('Equipo lleno, no puede agregar mas pokemones')
        else:
            self.equipo.append(pokemon)

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        if len(self.equipo) == 0:
            return 0
        total = 0
        for pokemon in self.equipo:
            total += pokemon.nivel
        return total / len(self.equipo)
