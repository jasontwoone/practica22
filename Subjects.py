# from analizador import *

class Subjets:
    def __init__(self, codigo, nombre, prerrequisito, obligatorio, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerequisito = prerrequisito
        self.obligatorio = obligatorio
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado

    def getCurso(self):
        print("__________________________________")
        print('codigo', self.codigo)
        print('nombre', self.nombre)
        print('prerequisito', self.prerequisito)
        print('obligatorio', self.obligatorio)
        print('semestre', self.semestre)
        print('creditos', self.creditos)
        print('estado', self.estado )

    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_prerrequisito(self):
        return self.prerequisito

    def get_obligatorio(self):
        return self.obligatorio

    def get_semestre(self):
        return self.semestre
    
    def get_creditos(self):
        return self.creditos
    
    def get_estado(self):
        return self.estado

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_codigo(self, codigo):
        self.codigo = codigo
        
    def set_prerrequisito(self, prerrequisito):
        self.prerequisito = prerrequisito
    
    def set_obligatorio(self, obligatorio):
        self.obligatorio = obligatorio

    def set_semestre(self, semestre):
        self.semestre = semestre
    
    def set_creditos(self, creditos):
        self.creditos = creditos
    
    def set_estado(self, estado):
        self.estado = estado
       
            
                
