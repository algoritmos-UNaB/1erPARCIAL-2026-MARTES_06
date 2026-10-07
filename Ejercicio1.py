class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int):
        self.nombre = nombre
        self.tipo = tipo
        # Garantizamos que el nivel esté entre 1 y 100
        self.nivel = max(1, min(100, nivel))

    def subir_nivel(self):
        """Incrementar el nivel del pokemon en 1 si es menor a 100."""
        if self.nivel < 100:
            self.nivel += 1

    def __str__(self):
        """Devuelve representacion en cadena en el formato requerido."""
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"


class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon: Pokemon):
        """Agregar un pokemon al equipo (maximo 6)."""
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print("el equipo ya tiene 6 pokemon no se puede agregar mas")

    def mostrar_equipo(self):
        """Imprime todos los pokemon del equipo utilizando su __str__."""
        if not self.equipo:
            print("el equipo esta vacio")
            return
        
        print(f"equipo de {self.nombre}:")
        for p in self.equipo:
            print(p)

    def nivel_promedio(self) -> float:
        """Calcula el nivel promedio del equipo."""
        if not self.equipo:
            return 0.0
        suma_niveles = sum(p.nivel for p in self.equipo)
        return suma_niveles / len(self.equipo)
