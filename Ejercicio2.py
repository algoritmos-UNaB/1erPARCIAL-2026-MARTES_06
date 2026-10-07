class PokemonNode:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.siguiente: PokemonNode = None
    def buscar_pokemon(nodo: PokemonNode, nombre_pokemon: str) -> bool:
        """
        funcion recursiva para buscar un pokemon especifico en la lista enlazada.
        Parametros:
        -nodo: PokemonNode (nodo actual donde se realiza la busqueda.)
        -nombre_pokemon: (Nombre del pokemon que se busca.)
        Retorno:
        -Devuelve true si se encuentra el pokemon, o False si no.
        """
        #(1)Logica: Si el nodo actual es None; devuelve False
        if nodo is None:
            return False
        #(2)Logica: Si el nombre del nodo actual coincide con nombre_pokemon, devuelve true.
        if nodo.nombre == nombre_pokemon
        return true
        #(3)Logica: LLama recursivamente a si mismapara buscar en la lista
        return buscar_pokemon(nodo.siguiente, nombre_pokemon)
        #Respuesta Teoria:
        #Tiempo de ejecucion (complejidad temporal/Orden lineal) donde N es el numero de nodos (pokemon) en la lista enlazada= La explicacion que da es que en el peor de los casos (Cuando el pokemon esta en el ultimo nodo o no existe en la lista), la funcion realiza una llamada recursiva por cada elemento existente en la estructura, evaluando N nodos individualmente.



