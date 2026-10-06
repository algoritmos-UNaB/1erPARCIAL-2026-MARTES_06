class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int):
        # Constructor que inicializa atributos del Pokemon.
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = max(1,min(nivel,100))
        # Asegura que el nivel esté entre 1 y 100
    
    def subir_nivel(self):
        # Sube el nivel del Pokemon de a uno en tanto no supere el nivel 100 luego de la suma
        if self.nivel < 100:
            self.nivel +=1
    
    def __str__(self) -> str:
        # Devuelve una cadena con los datos del Pokemon
        return f"Nombre:{self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"
class Entrenador:
    def __init__(self, nombre: str):
        # Constructor que inicializa nombre del entrenador y genera un equipo como lista vacía
        self.nombre = nombre
        self.equipo = []
    
    def agregar_pokemon(self, pokemon: Pokemon):
        #  que agrega pokemones a la lista por un append
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
            # Límite de 6 pokemones por equipo
        else:
            print("No se pueden tener más de 6 pokemones")
    def mostrar_equipo(self):
        print(f"Equipo de {self.nombre}:")
        if not self.equipo:
            # Caso para equipo vacío
            print("El equipo no tiene pokemones")
            return
        for pokemon in self.equipo:
            print(pokemon)
    
    def nivel_promedio(self) -> float:
        #  que promedia los niveles del equipo del entrenador
        if not self.equipo:
            return 0.0
        suma_niv = sum(pokemon.nivel for pokemon in self.equipo)
        return suma_niv /len(self.equipo)
