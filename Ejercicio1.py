class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
            print(f"El pokemon {self.nombre} subio {self.nivel}.")
        else:
            print(f"{self.nombre} ya esta en el nivel maximo (100).")

    def str(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"

class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = [] 

    def agregar_pokemon(self, pokemon: Pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
            print(f"{pokemon.nombre} ha sido agregado al equipo de {self.nombre}.")
        else:
            print(f"No se puede agregar a {pokemon.nombre}. El equipo de {self.nombre} ya tiene 6 Pokemon.")

    def mostrar_equipo(self):
        print(f"\n--- Equipo de {self.nombre} ---")
        if not self.equipo:
            print("El equipo esta vacio.")
        else:
            for pokemon in self.equipo:
                print(pokemon)

    def nivel_promedio(self):
        if not self.equipo:
            return 0
        
        suma_niveles = sum(pokemon.nivel for pokemon in self.equipo)
        promedio = suma_niveles / len(self.equipo)
        return promedio