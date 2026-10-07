class Pokemon:
    def __init__(self, nombre,tipo,nivel):
        self.nombre = nombre
        self.tipo=tipo

        if nivel >= 1 and nivel <= 100:
            self.nivel=nivel
        else:
            raise ValueError("Nivel incorrecto")

    def subir_nivel(self):
        if self.nivel <100:
           self.nivel = self.nivel + 1

    def __str__(self):
       return f"Nombre: {self.nombre},Tipo: {self.tipo}, Nivel:{self.nivel}"
    
class Entrenador:

    def __init__(self, nombre):
        self.nombre=nombre
        self.equipo=[]

    def agregar_pokemon(self,pokemon):
        if len(self.equipo)<6:
            self.equipo.append(pokemon)
        else:
            print("No mas pokemon en el equipo")

    def mostrar_equipo(self):
        for equi in self.equipo:
            print(equi)

    def nivel_promedio(self):
        if len(self.equipo)==0:
            return 0

        suma_niveles=0

        for equi in self.equipo:
            suma_niveles = suma_niveles +equi.nivel
        
        promedio = suma_niveles / len(self.equipo)

        return promedio

