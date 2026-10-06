class PokemonNode:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

def buscar_pokemon(nodo, nombre_pokemon):
    if nodo is None:
        return False
    if nodo.nombre == nombre_pokemon:
        return True

    
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)

    # Respuesta a la teoria: El tiempo estimado de ejecucion de la funcion recursiva buscar_pokemon() es O (N) o de orden lineal, 
    #esto significa que el programa va recorriendo uno por nodo hasta encontrar el pokemon, pudiendo estar el pokemon en el ultimo
    # nodo o que no esté en la lista, no le queda más que recorrer hasta el último nodo.