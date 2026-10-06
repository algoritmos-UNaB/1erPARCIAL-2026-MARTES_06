class Evolucion:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None #puntero

class PilaEvoluciones:
    def __init__(self):
        self.evoluciones = None
        #tope de pila
    
    def apilar(self):
        #se genera un nuevo nodo que apunta al antiguo tope convirtiendose en el nuevo tope
        evolucion.siguiente = self.evoluciones
        self.evoluciones = evolucion
    
    def desapilar(self):
        #agregado de caso sin evoluciones
        if self.evoluciones is None:
            return "No hay evoluciones para desapilar"
        eliminado = self.
        #se mueve el tope al nodo siguiente
        self.evoluciones = self.evoluciones.siguiente
        return eliminado

    def mostrar_evoluciones(self):
        actual.self.evoluciones
        #caso sin evoluciones
        if actual is None:
            print("No hay evoluciones que mostrar")
        return
        #caso con alguna evolución
        print("Todas las evoluciones:")
        while actual is not None:
            print(f"- {actual.nombre}")
            actual = actual.siguiente
    
    def __iter__(self):
        #Retorna el iterador
        return IteradorPilaEvoluciones(self.evoluciones)

class IteradorPilaEvoluciones:
    def __init__ (self, inicio: Evolucion):
        #primer nodo donde inicia la iteración
        self.actual = inicio

    def __next__(self):
        #caso de excepcion al llegar al final de la pila
        if self.actual is None:
            raise StopIteration
        #Se mueve el puntero al siguiente elemento de la pila
        self.actual = self.actual.siguiente
        return resultado
