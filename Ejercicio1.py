class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        #Validación
        if nivel < 1:
            self.nivel = 1 
            elif nivel > 100:
                self.nivel = 100
                else:
    self.nivel = nivel
    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"
        
