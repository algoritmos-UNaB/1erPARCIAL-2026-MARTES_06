class pokemon:
    def __init__(self, nombre:str, tipo: str, nivel:int)
    self.nombre= nombre
    self.tipo= tipo
    self.nivel= self.nivel_valido (nivel)
    def nivel_valido(self, nivel:int)
    if (1> nivel >100)
    raice ValueError (f"el nivel de {self.nombre} debe estar entre 1 y 100)
    return nivel
    def __repr__(self):
        return f"pokemon({self.nombre}, {self.tipo},{self.nivel})
        
class entrenador: 