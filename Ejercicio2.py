class PokemonNode :

    def __init__ (self, nombre: str) :

        self.nombre = nombre
        self.siguiente = None


def buscar_pokemon (nodo: PokemonNode, nombre_pokemon: str) -> bool :

    if nodo is None :

        return f"{nombre_pokemon} | {False}"

    if nodo.nombre == nombre_pokemon:

        return f"{nombre_pokemon} | {True}"

    return buscar_pokemon (nodo.siguiente, nombre_pokemon)


#TEST

app = PokemonNode ("Pikachu")
app.siguiente = PokemonNode ("Charizard")
app.siguiente.siguiente = PokemonNode ("Squirtle")

print ("==== Recursividad ====")
print (buscar_pokemon (app, ("Squirtle")))
print (buscar_pokemon (app, ("Rookidee")))
print (buscar_pokemon (None, ("Pikachu")))


"""Teoría: Cuál es el tiempo de ejecución estimado de la función buscar_pokemon()?
    - Respuesta: tarda dependiendo de la cantidad de nodos que tenga para recorrer, en este caso (3)
    nodos hace 3 comprobaciones, si el nodo se duplica tambien se duplica el tiempo que tarda la funcion en buscar
    el pokemon.
"""

"""Nombre y Apellido: RODRIGO MATIAS LOPEZ
Email: rodlopez003@gmail.com
Comisión: 1"""