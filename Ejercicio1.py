class Pokemon():
    def __init__(self, nombre:str, tipo:str, nivel:int):
        if type(nombre) != str:
            raise TypeError("El nombre debe ser un string..")
        elif type(tipo) != str:
            raise TypeError("El tipo debe ser un string..")
        elif type(nivel) != int:
            raise TypeError("El nivel debe ser un número..")
        elif nivel < 1 or nivel > 100:
            raise ValueError("El nivel de su pokemon debe estar entre 1 y 100..")

        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
        else:
            print("Su poemón alcanzó el máximo nivel! Felicidades!!") 
    
    def __str__(self):
        return(f"Nombre: '{self.nombre}', Tipo: '{self.tipo}', Nivel: '{self.nivel}'.")


class Entrenador():
    def __init__(self, nombre:str):
        if type(nombre) != str:
            raise TypeError("El nombre debe ser un string..")
        self.equipo = []
        self.nombre= nombre

    def agregar_pokemom(self, pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print(f"¡{self.nombre}, has completado tu equipo! No puedes agregar a {pokemon.nombre}..")
    
    def mostrar_equipo(self):
        for pokoemon in self.equipo:
            print(f"\n{pokemon}")
    
    def nivel_promedio(self):
        if len(self.equipo) == 0:
            return 0
        
        nivel_total = 0
        for pokemon in self.equipo:
            nivel_total += pokemon.nivel
        
        promedio = round(nivel_total / len(self.equipo),2)
        return promedio
    


