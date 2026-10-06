# Ejercicio 2: Recursividad

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

# - Teoría: Cuál es el tiempo de ejecución estimado de la función <code>buscar_pokemon()</code>?
# Es 0(n), donde n es la cantidad de nodos de la lista. En el peor caso, el Pokémon está al final o no está, la función revisa todos los nodos, una vez cada uno. Y en el mejor caso, está en el primero y solo revisa uno.
