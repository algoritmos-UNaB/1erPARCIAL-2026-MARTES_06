class pokemon:
    def__init__(self, nombre:str, tipo: str, nivel: iny):
        self.nombre = nombre
        self.tipo = tipo

        if nivel<1:
            self.nivel = 1
        elif nivel >100:
            self.nivel =100
        else:
            self.nivel = nivel

    def subir_nivel(self):
      if self.nivel <100:
        self.nivel +=1

   def __str__(self):
     return 

class entrenador:
    def__init__(self,nombre: str):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon: pokemon):
       if len(self.equipo) >=6:
         print("")
     else:
            self.equipo.append(pokemon)

    def mostrar_equipo(self):
       for poke in self.equipo:
         print(str(poke))

    def nivel_promedio(self)_float:
      if not self.equipo:
        return 0.0
        suma_niveles = 0
         for poke in self.equipo:
            suma_niveles += poke.nivel
         return suma_niveles/ len(self.equipo)
