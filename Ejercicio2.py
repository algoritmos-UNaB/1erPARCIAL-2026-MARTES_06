class PokemonNode:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None  # Instancia de PokemonNode o None


def buscar_pokemon(nodo: PokemonNode, nombre_pokemon: str) -> bool:
    """
    Busca de manera recursiva un Pokemon por su nombre en la lista enlazada.
    """
    # Caso base 1: Llegamos al final de la lista o el nodo actual es None
    if nodo is None:
        return False
    
    # Caso base 2: Se encuentra el Pokemon en el nodo actual
    if nodo.nombre.lower() == nombre_pokemon.lower():
        return True
    
    # Paso recursivo: Buscar en el siguiente nodo de la lista
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)


"""
--- PREGUNTA EJERCICIO 2---
¿Cual es el tiempo de ejecucion estimado de la funcion buscar_Pokemon()?

Respuesta:
El tiempo de ejecucion estimado es O(n), donde 'n' es el numero total de nodos (Pokemon)
en la lista enlazada.

Explicacion:
En el peor de los casos (cuando el Pokemon no esta en la lista o se encuentra en el ultimo nodo),
la funcion realiza una llamada recursiva por cada elemento de la lista enlazada, procesando cada
nodo en tiempo constante O(1). Por lo tanto, la complejidad temporal crece de manera lineal con
respecto al tamano de la lista.
"""