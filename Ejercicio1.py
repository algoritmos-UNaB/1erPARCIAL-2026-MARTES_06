"""
Ejercicio 1: Implementación de TADs
En este universo, cada entrenador tiene un equipo Pokémon. Para este ejercicio deberá implementar dos clases en Python: Pokemon y Entrenador.

Clases a Implementar
Clase Pokemon:

Atributos:

nombre : str : Nombre del Pokémon.
tipo : str: Tipo del Pokémon (por ejemplo, Agua, Fuego, Planta).
nivel : int: Nivel del Pokémon (debe estar entre 1 y 100).
Métodos:

init(): Constructor que inicializa los atributos del Pokémon.
subir_nivel(): Método que incrementa el nivel del Pokémon en 1, siempre y cuando no supere el nivel 100.
str(): Método que devuelve una representación en cadena del Pokémon en el formato: "Nombre: Pikachu, Tipo: Electrico, Nivel: 0"
Clase Entrenador:

Atributos:
nombre : str: Nombre del entrenador.
equipo : list: Lista que contiene instancias de la clase Pokemon.
Métodos:
init(): Constructor que inicializa el nombre del entrenador y crea una lista vacía para el equipo.
agregar_pokemon(): Método que agrega un Pokémon al equipo. Si ya hay 6 Pokémon en el equipo, debe mostrar un mensaje indicando que no se pueden tener más Pokémon.
mostrar_equipo(): Método que imprime todos los Pokémon del equipo utilizando el método str de la clase Pokemon.
nivel_promedio(): Método que calcula y devuelve el nivel promedio de los Pokémon en el equipo. Si no hay Pokémon en el equipo, debe devolver 0.
"""

class Pokemon:
    NIVEL_MIN = 1
    NIVEL_MAX = 100

    def __init__(self, nombre: str, tipo:str, nivel:int):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
     
     
def subir_nivel(self):
        if self.nivel < self.NIVEL_MAX:
            self.nivel +=1
        else: print("error")

def __str__(self):
     return f"Nombre {self.nombre}, tipo: {self.tipo}, nivel: {self.nivel}"


class Entrenador:
     MAX_EQUIPO = 6
     def __init__(self, nombre: str):
          self.nombre = nombre
          self.equipo = []
     def agregar_pokemon(self, pokemon: Pokemon):
        if len(self.equipo) >= self.MAX_EQUIPO:
            print(f"{self.nombre} ya tiene {self.MAX_EQUIPO} Pokémon. No se pueden tener más.")
        else:
            self.equipo.append(pokemon)
     def mostrar_equipo(self):
          if not self.equipo:
               print(f"{self.nombre} no tiene Pokémon en su equipo.")
               return
          print(f"Equipo de {self.nombre}:")
          for pokemon in self.equipo:
            print(pokemon)

     def nivel_promedio(self):
        if not self.equipo:
            return 0
        return sum(p.nivel for p in self.equipo) / len(self.equipo)