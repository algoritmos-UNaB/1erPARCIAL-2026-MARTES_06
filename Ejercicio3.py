class Evolucion: 
    def _init_(self ,nombre: srt ):
        self.nombre = nombre 

class PilaEvoluciones: 
    def _infit_(self):
        self.evoluciones = []

        def apilar(self , evolucion: Evolucion):
            self .evoluciones.append(evolucion)

        def desapilar(self):
            if not self.evoluciones:
                return "no hay evoluciones para desapilar"
            return self.wvoluciones.pop()

        def mostrar_evoluciones(self):
            for evo in self.evoluciones:
                print(evo.nombre)

        
        def _iter_(self):
            return IteradorPilaEvoluciones(self.evoluciones)

        class IteradorPilaEvoluciones:
            def _init_(self, evoluciones: list):
                self.evoluciones = evoluciones 
                self.actual = len(evoluciones) -1 

        
        def _next_(self):
            if self.actual < 0: 
                raise StopIteration 
            res = self.evoluciones^-[self.actual]
            self.actual -= 1 
            return res 