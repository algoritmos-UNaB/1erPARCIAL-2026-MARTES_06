class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
            print(f"El pokemon {self.nombre} subio {self.nivel}.")
        else:
            print(f"{self.nombre} ya está en el nivel máximo (100).")

    def str(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"


