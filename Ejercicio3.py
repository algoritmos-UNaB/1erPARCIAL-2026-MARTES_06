class Evolucion:
    #nodo de pila
    def __init__ (self, nombre: str) :

        self.nombre = nombre
        self.siguiente = None #referencia al nodo de abajo


class PilaEvoluciones:

    def __init__ (self) :
        
        self.evoluciones = None #tope de la pila

    def apilar (self, evolucion: Evolucion) :

        evolucion.siguiente = self.evoluciones #nuevo nodo apunta al tope actual
        self.evoluciones = evolucion #nuevo tope


    def desapilar (self) :
        #si no hay tope la pila esta vacia y no tiene nada para sacar
        if self.evoluciones is None :

            return "No hay evoluciones para desapilar"

        tope = self.evoluciones #se guarda el tope actual
        self.evoluciones = tope.siguiente #nuevo tope
        tope.siguiente = None #se desconecta el nodo

        return tope

    def mostrar_evoluciones (self) :
        #recorre la pila
        for evolucion in self :

            print (evolucion.nombre)

    def __iter__ (self) :
        #usa la pila con un for
        return IteradorPilaEvoluciones (self.evoluciones)


class IteradorPilaEvoluciones :

    def __init__ (self, actual: Evolucion) :
        
        self.actual = actual #nodo actual

    def __iter__ (self) :

        return self

    def __next__ (self) :
        #si no hay nodos termina con el for
        if self.actual is None :

            raise StopIteration 
        
        valor = self.actual #guarda el nodo actual para devolverlo
        self.actual = self.actual.siguiente

        return valor


"""Nombre y Apellido: RODRIGO MATIAS LOPEZ
Email: rodlopez003@gmail.com
Comisión: 1"""