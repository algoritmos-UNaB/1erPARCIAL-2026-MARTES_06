class PokemonNode :
    #nodo
    def __init__ (self, nombre: str) :

        self.nombre = nombre
        self.siguiente = None #referencia al nodo siguiente


def buscar_pokemon (nodo: PokemonNode, nombre_pokemon: str) -> bool :

    if nodo is None : #si no encuentra nada en la lista o esta vacia, devuelve false

        return False

    if nodo.nombre == nombre_pokemon: #si tiene un pokemon, devuelve true

        return True 

    return buscar_pokemon (nodo.siguiente, nombre_pokemon) #caso recursivo para el siguiente nodo


"""Teoría: Cuál es el tiempo de ejecución estimado de la función buscar_pokemon()?
    - Respuesta: tarda dependiendo de la cantidad de nodos que tenga para recorrer, en este caso (3)
    nodos hace 3 comprobaciones, si el nodo se duplica tambien se duplica el tiempo que tarda la funcion en buscar
    el pokemon.
"""

"""Nombre y Apellido: RODRIGO MATIAS LOPEZ
Email: rodlopez003@gmail.com
Comisión: 1"""