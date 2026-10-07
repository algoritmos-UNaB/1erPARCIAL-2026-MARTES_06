class Pokemon:
    def __init__(self, name: str, type: str, nivel: int):
        if nivel <1 or nivel > 100:
            raise ValueError("El nivel del pokemon debe ser del 1 al 100")

        self.name = name
        self.type = type
        self.nivel = nivel
    
    def subir_nivel(self):
        if self.nivel < 100: 
            self.nicel += 1
    
    def __str__(self):
        return f"{self.name} - Tipo: {self.tipo} - Nivel: {self.nivel}"
    
class Entrenador:
    def __init__(self, nombre: str, equipo: list):
        self.nombre = nombre
        self.equipo = []

   def agregar_pokemon(self, Pokemon):
    if len(self.equipo) >= 6:
        print("tu equipo esta lleno, el pokemon sera enviado al PC")
    else:
        self.equipo.apped(Pokemon)
    
    def mostrar_equipo(self):
        dor Pokemon in self.equipo:
        print (Pokemon)
    
    def nivel_promedio (self):
        if len(self.equipo) ==0:
            return 0

        suma = 0

        for Pokemon in self.equipo:
            sema += Pokemon.nivel


    
