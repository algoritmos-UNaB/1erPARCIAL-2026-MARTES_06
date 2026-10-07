Pokémon

class Pokemon:
    def __init__(self, nombre, tipo,nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

   def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1


Entrenador

class Entrenador:
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo

   def agregar_pokemon(self):
        
   def mostrar_equipo(self):

   def nivel_promedio(self):
