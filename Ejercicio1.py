atributos pokemon
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
metodos
    def aumentar_nivel(self):
        if nivel<100
        self.nivel +=1


class entrenador:
    def __init__(self, nombre_entrenador: str, ): 
        self.nombre_entrenador= nombre_entrenador
        self.equipo= []
    def agregar_pokemon (self, pokemon: pokemon)
        if len(self.equipo)<=6
        self.equipo.append(pokemon)
    else print("el equipo de {nombre_entrenador} no puede tener mas pokemons, el maximo es 6")
    def mostrar_equipo(self):
        if self.equipo==0:
        print(f"el equipo de {nombre_entrenador} esta vacio")
        else :
        print(f"\nEquipo de {nombre_entrenador}")
        for pokemon in self.equipo:
            print(pokemon)
    def promedio_nivel (self)-> float:
        ifnot self.equipo:
            return 0.0
        return

