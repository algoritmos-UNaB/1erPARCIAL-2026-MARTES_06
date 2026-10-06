# Ejercicio 2: Recursividad en el Universo Pokémon

class PokemonNode:

    def __init__(self, nombre, siguiente=None):
        self.nombre = nombre
        self.siguiente = siguiente

    def buscar_pokemon(nodo: PokemonNode, nombre_pokemon: str):
        if nodo is None:
            return False

        if nodo.nombre == nombre_pokemon:
            return True

        return buscar_pokemon(nodo.siguiente, nombre_pokemon)