class Pokemon:
    def __init__(self,nombre:str,tipo:str,nivel:int):
        self.nombre=nombre
        self.tipo=tipo
        self.nivel=nivel
        if nivel >100:
            self.nivel=100
        elif nivel < 1 :
            self.nivel=1
        else:
            self.nivel=nivel

    def subir_nivel(self,nivel):
        if self.nivel <100:
            self.nivel +=1
        else:
            print("numeros permitidos del 1 al 100")

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel} "

class Entrenador:
    def __init__(self,nombre):
        self.nombre=nombre
        self.equipo=[]

    def agregar_pokemon(self,pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print("no se pueden tener mas de 6 pokemons en el equipo")

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        if len(self.equipo) == 0:
            return 0 

        suma_niveles= 0 
        for pokemon in self.equipo:
            suma_niveles += pokemon.nivel

        return suma_niveles/len(self.equipo)

    
        

    

