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
class Entrenador:
    def__init__(self, nombre):
        self.nombre = nombre
        self.equipo = []
        
def agregar_pokemon(self, pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print("No se puede tener más Pokémon.")
                def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        if len(self.equipo) == 0:
        
        suma = 0
        for p in self.equipo:
            suma += p.nivel
            
        promedio = suma / len(self.equipo)
        return promedio

