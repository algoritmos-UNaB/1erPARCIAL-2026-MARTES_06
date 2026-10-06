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
     def __inti__(self, nombre, tipo, nivel):
          self.nombre = nombre
          self.tipo = tipo
          self.nivel = nivel
     def subir_nivel(self, nivel):
          if self.nivel > 100 then self.nivel + 1
     
     def str(self):
          print(f"El pokemon en {self.nombre} su tipo es {self.tipo} tiene un nivel de poder de {self.nivel}")


     