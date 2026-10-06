class PokemonNode :

    def __init__ (self, nombre: str) :

        self.nombre = nombre #nombre que guarda el nodo
        self.siguiente = None #referencia al proximo nodo


def buscar_pokemon (nodo: PokemonNode, nombre_pokemon: str) -> bool :
    #si la lista esta vacia o no encuentra el nombre, no existe el pokemon
    if nodo is None :

        return f"{nombre_pokemon} | {False}"

    if nodo.nombre == nombre_pokemon:
        #nodo actual tiene el nombre actual del pokemon y devuelve verdadero porque se encontro
        return f"{nombre_pokemon} | {True}"
    #caso recursivo, se repite la busqueda con el nodo siguiente
    return buscar_pokemon (nodo.siguiente, nombre_pokemon)


"""Teoría: Cuál es el tiempo de ejecución estimado de la función buscar_pokemon()?
    - Respuesta: tarda dependiendo de la cantidad de nodos que tenga para recorrer, en este caso (3)
    nodos hace 3 comprobaciones, si el nodo se duplica tambien se duplica el tiempo que tarda la funcion en buscar
    el pokemon.
"""

"""Nombre y Apellido: RODRIGO MATIAS LOPEZ
Email: rodlopez003@gmail.com
Comisión: 1"""