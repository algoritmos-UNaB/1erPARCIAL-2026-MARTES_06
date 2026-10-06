## Ejercicio 1: Implementación de TADs

class Pokemon:
    def __init__ (self, nombre, tipo, nivel):
    def subir_de nivel
        if self.nivel < 100
            self.nivel +=1
    def _str_(self):
        return f'Nombre:{self.nombre}, Tipo:{self.tipo}, Nivel{self.nivel}'
class Entrenador:
    def __init__ (self, nombre):
        self.nombre=nombre
        self.equipo=[]
    def agregar_pokemon (self, pokemon):
        if len(self.equipo)< 6:
            self.equipo.append
        else:
            print('El entrenador no puede tener mas pokémons')
    def mostrar_equipo(self):
        if len(self.equipo)== 0:
            return 0
        niveles=0
        for pokemon in self.equipo:
            total_niveles+=pokemon.nivel
        return total_niveles/len(self.equipo)

