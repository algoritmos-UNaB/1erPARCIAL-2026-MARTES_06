class PokemonNode:
    
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None

    def buscar_pokemon(self, nodo, nombre_pokemon: str):

        if nodo is None:
            return False

        if nodo.nombre == nombre_pokemon:
            return True

        return buscar_pokemon(nodo.siguiente, nombre_pokemon)


# El tiempo de ejecucion es O(n), donde se recorren todos los nodos de la lista hasta encontrar el Pokemon o llegar al final y comprobar que no se encuentra.