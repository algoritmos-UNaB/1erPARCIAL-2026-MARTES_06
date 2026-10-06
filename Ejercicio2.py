class PokemonNode:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None

def buscar_pokemon(nodo, nombre_pokemon: str):
    if nodo is None:
        return False
    elif nodo.nombre == nombre_pokemon:
        return True
    else:
        return buscar_pokemon(nodo.siguiente, nombre_pokemon)

#Teoria: Cual es el tiempo de ejecucion estimado de la funcion buscar_pokemon()?
#Respuesta: El tiempo es proporcional a la cantidad de elementos (en este caso nodos) que tenga en mi lista hasta encontrar el pokemon. 