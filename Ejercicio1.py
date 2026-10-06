class Pokemon:
   def __init__ (self, nombre, tipo, nivel):
       self.nombre= nombre
       self.tipo= tipo
       self.nivel= nivel 

    def subir_nivel(self):
        if self.nivel < 100:
           self.nivel += 1
    
    def __str__(self):
        return f"nombre: {self.nombre}, tipo: {self.tipo}, nivel: {self.nivel}"


  class Entrenador:
    def __init__ (self, nombre):
        self.nombre= nombre
        self.equipo= [] 
            