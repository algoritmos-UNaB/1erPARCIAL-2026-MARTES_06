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
    def __init__(self, nombre: str, equipo: list)
    