

class PokemonNode:
    ded __init__(self, nombre):
        self.nombre=nombre
        self.siguiente=None

def buscar_pokemon(nodo,nombre):
    if nodo is None
        return False
    if nodo.nombre==nombre:
        return True
    return buscar_pokemon(nodo.siguiente, nombre)

#- Teoría: Cuál es el tiempo de ejecución estimado de la función <code>buscar_pokemon()</code>?
#-La funcion revisa cada elemento de la lista hasta el final, asi que va a depender de cuantos haya. 
# Podriamos establecer el tiempo de inicio y fin de la ejecusion y restar la diferencia.