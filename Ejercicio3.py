class evolucion:
    def__init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None 

class iteradorpilaevoluciones:
    def__init__(self, actual: evolucion):
        self.actual = actual

    def __next__(self): 
       if self.actual is None:

evolucion_actual = self.actual
self.actual = self.actual.siguiente
return evolucion_actual

class pilaevoluciones:
    def__init__(self):
        self.evoluciones = None

    def apilar(self, evolucion: evolucion):
        evolucion.siguiente = self.evoluciones
        self.evoluciones = evolucion

    def desapilar(self):
        if self.evoluciones is None:
            return

        evolucion_eliminada = self.evoluciones
        self.evoluciones = self.evoluciones.siguiente
        return evolucion_eliminada

    def mostrar_evoluciones(self):
        actual = self.evoluciones
        while actual is not None:
            print(actual.nombre)
            actual = actual.siguiente

    def __inter__(self)
        return iteradorpilaevoluciones(self.evoluciones)