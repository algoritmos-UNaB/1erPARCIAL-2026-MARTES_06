class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = max(1,min(nivel,100))
    
    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel +=1
    
    def __str__(self) -> str:
        return f"Nombre:{self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"
class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = []
    
    def agregar_pokemon(self, pokemon: Pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print("No se pueden tener más de 6 pokemones")
    def mostrar_equipo(self):
        print(f"Equipo de {self.nombre}:")
        if not self.equipo:
            print("El equipo no tiene pokemones")
            return
        for pokemon in self.equipo:
            print(pokemon)
    
    def nivel_promedio(self) -> float:

        if not self.equipo:
            return 0.0
        suma_niv = sum(pokemon.nivel for pokemon in self.equipo)
        return suma_niv /len(self.equipo)
