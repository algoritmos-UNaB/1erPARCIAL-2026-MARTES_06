class PokemonNode:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None


def buscar_pokemon(nodo: PokemonNode, nombre_pokemon: str):
    if nodo is None:
        return False
    
    if nodo.nombre == nombre_pokemon:
        return True
    
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)


# Teoría: Cuál es el tiempo de ejecución estimado de la función buscar_pokemon()?
# Respuesta: El tiempo de ejecución etimado es de complejidad lineal, es decir, O(n). Esto teniendo en cuenta el peor caso en que el pokemon no se -
# encuentre, en cuyo caso debera recorrer cada nodo para el cual debe realizar una nserie de operaciones primitivas las cuales aumentan de forma 
# proporcional