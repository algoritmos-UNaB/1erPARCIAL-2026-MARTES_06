class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        if nivel > 100 or nivel < 1: 
            raise ValueError("El nivel del pokemon debe estar entre los niveles 1 a 100")
        self.nivel = nivel

    def subir_nivel(self):
        
        if self.nivel == 100: 
            print("Tu pokemon ya alcanzo su maximo nivel! - Intenta subir de nivel otro!")
        else:
            self.nivel += 1

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"       


class Entrenador:
    def __init__(self, nombre):    
        self.nombre = nombre        
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        if len(self.equipo) >= 6 :
            print("No se puede agregar tu pokemon por que ya tienes 6 pokemons en tu equipo!!")
        else:
            self.equipo.append(pokemon)

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        if len(self.equipo) < 1 :
            return 0
        else:    
            sumador = 0
            for pokemon in self.equipo:
                sumador += pokemon.nivel
            
            resultado = sumador / len(self.equipo)
            return resultado