class Pokemon:
    def init(self ,nombre: str, tipo: str ,nivel: int= 1 ):
        self.nombre = nombre 
        self.tipo = tipo 
        if nivel < 1:
            self.nivel = 1
        elif nivel > 100:
            self.nivel = 100
        else:
            self.nivel = nivel 

    def subir_nivel (self):
        if self.nivel <100:
            self.nivel + 1 
    
    def _str_(self):
        return "nombre: {self.nombre} , tipo {self.tipo} , nivel: {self.nivel}

    class Entrenador:
        def _init(self , nombre : srt) 
        self.nombre = nombre 
        self.equipo = [] 

    def agregar _ pokemon(self,p):
        if len (self.equipo) >= 6:
            print("no se puede tener mas pokemon en el equipo ")
        else:
            self.equipos.append(p)


    def nivel_prometido(self):
        if len(self.equipo)  == 0:
            return 0 

            suma_niveles = 0 
        for p in self.equipo:
            suma_niveles = suma_niveles + p.nivel 
        return suma_niveles / len(self.equipo)    