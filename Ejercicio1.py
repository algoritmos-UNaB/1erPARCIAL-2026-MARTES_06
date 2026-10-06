#EN ESTE UNIVERSO CADA ENTRENADOR TIENE SU EQUIPO POKEMON

#EQUIPO POKEMON

class POKEMON:

  def _init_(self, nombre: str, tipo: str, nivel: int):
      self.nombre = nombre
      self.tipo = tipo
      self.nivel = nivel

  def _subir_nivel(self):
    if 1 <= nivel <= 100
            self.nivel = nivel
        elif nivel < 1:
            self.nivel = 1
    else=100

  def __str__(self)
      return f"Pokémon: {self.nombre} | Tipo: {self.tipo} | Nivel: {self.nivel}"


#ENTRENADOR

class ENTRENADOR:

 def _init_(self, nombre: str, equipo: list)
     self.nombre = nombre
     self.equipo = equipo

 def agregar_pokemon