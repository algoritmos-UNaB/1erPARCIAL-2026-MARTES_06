class Pokemon:

    def __init__(self, nombre: str, nivel: int):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel =max(1, min(100, nivel1))
    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
    def __str__(self):
        return f""Nombre:{self.nombre}, Tipo:{self.tipo}, Nivel:{self.nivel}"

class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo =[]
   def agregar_pokemon(self, pokemon: Pokemon):
    if len(self.equipo)< 6:
        self.equipo.append(pokemon)
        else:
            print(f"Aviso: {self.nombre} ya tiene 6 pokemones en su equipo no se puede tener más."
    def mostrar_equipo(self):
        