class Pokemon:
    def __init__(self,nombre,tipo,nivel):
        self.nombre=nombre
        self.tipo=tipo
        self.nivel=nivel
    
    def subir_nivel():
        if self.nivel < 100:
            self.nivel += 1

Amoonguss= Pokemon("Amoonguss","Planta/Veneno",20)
Pikachu= Pokemon("Pikachu","Electrico",3)
Jigglypuff=Pokemon("Jigglypuff","normal/Hada",45)
Charmander=Pokemon("Charmander","Fuego",98)
Bulbasaur=Pokemon("Bulbasaur","Planta/Veneno",67)
Squirtle=Pokemon("Squirtle","Agua",12)
Eevee=Pokemon("Eevee","normal",76)
Rattata=Pokemon("Rattata","normal",27)
Psyduck=Pokemon("Psyduck","Agua",18)

class Entrenador:
    def __init__(self,nombre):
    self.nombre = nombre
    self.equipo = []

    def agregar_pokemon(self,pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print("Equipo lleno,no se pueden agregar mas pokemones")
    

    def mostrar_equipo(self,equipo):
        for pokemon in self.equipo:
            print(str(pokemon))

    def nivel_promedio(self):
        if len(self.equipo) == 0:
            return 0
        suma=0
        for pokemon in self.equipo:
            suma += pokemon.nivel
        return suma / len(self.equipo)

Ash=Entrenador("Ash")
