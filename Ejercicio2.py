#Recursividad en el Universo Pokémom

class PokemonNode:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None

def buscar_pokemon(nodo, nombre_pokemon):
    if nodo is None:
        return False
    if noto.nombre == nombre_pokemon:
        return True
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)