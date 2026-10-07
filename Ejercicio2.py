class PokemonNode:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


def buscar_pokemon(nodo, nombre_pokemon):
    # Caso 1: lista finalizada  o vacia
    if nodo is None:
        return False
    
    # Caso 2: si encuentra pokemon en el nodo actual
    if nodo.nombre == nombre_pokemon:
        return True
    
    # Paso recursivo: se sigue buscando en el siguiente nodo
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)

