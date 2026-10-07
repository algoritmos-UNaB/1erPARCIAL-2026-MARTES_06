class Evolucion:
 def __init__(self, nombre: str):
  self.nombre = nombre
  self.siguiente = None

  class IteradorPilaEvoluciones:
    def __init__(self, actual: Evolucion):
     self.actual = actual

def __init__ (self):
 return self

def __next__ (self):
"""Retorna el siguiente valor y actualiza el puntero actual"""
if self.actual is None:
 raise StopIteration
  
valor = self.actual.nombre
self.actual.siguiente
return valor

class IteradorPilaEvoluciones
def __init__ (self):
    self.tope = None

def mostrar_evoluciones(self):
 """Imprime todas las evoluciones recorriendo la pila."""
if self.tope is None:
 print("No hay evoluciones en la pila.")
 return

print("Evoluciones registradas (de mas reciente a mas antigua):")
for evo in self:
print(f"- {Evolucion}")

def __iter__(self):
 """Retorna el iterador para poder usar la pila en un ciclo for."""
return IteradorPilaEvoluciones(self.tope)
