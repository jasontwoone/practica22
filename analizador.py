import readline
from Subjects import *
from tkinter import messagebox
from Subjects import *




class AnalizadorLexico:
    def __init__(self):
        self.listaCursos = [ ]

    
    def analizador(self,cadena):
        self.listaCursos = [ ]
        a = 0
        for linea in cadena:
 
            buffer = ""
            
            estadoAN = "A"
            codigo = ""
            nombre = ""
            prerrequisito = ""
            obligatorio = ""
            semestre = ""
            creditos = ""
            estado = ""
            contador = 0
            linea += '#'

            

            for caracter in linea:
                if estadoAN == 'A':
                    
                    if caracter != ',' and caracter != '#' :
                        # if caracter == ';':
                        #     buffer += ';'
                        buffer += caracter
                    elif caracter == ',':
                        contador +=1
                        if contador == 1:
                            codigo = buffer
                            buffer = ""
                        elif contador == 2:
                            nombre = buffer
                            buffer = ''
                        elif contador == 3:
                            
                            if buffer == '':
                                buffer = ''
                            else:
                                prerrequisito = buffer
                                buffer = ''
                        elif contador == 4:
                            obligatorio = buffer
                            buffer = ''
                        elif contador == 5:
                            semestre = buffer
                            buffer = ''
                        elif contador == 6:
                            creditos = buffer
                            buffer = ''     
                    elif caracter =='#':
                        estado = buffer
                        buffer = ''

                        
                            
                                

                        if int(obligatorio) == 1 or int(obligatorio) == 0 or int(obligatorio) == -1:
                                
                            if int(semestre) >= 1 or semestre <= 10:
                                if int(estado) == 1 or int(estado) == 0 or int(estado) == -1:                            

                                    

                                    
                                    self.listaCursos.append(Subjets(str(codigo),str(nombre),str(prerrequisito),str(obligatorio),str(semestre),str(creditos),str(estado)))
                                    

                                        
                                        # if Subjets.get_codigo(self) == codigo:
                                        #     self.listaCursos.remove(Sub)
            
                                    
                                else:
                                    messagebox.showinfo('Popup', ' Error rango estado')                            
                            else:messagebox.showinfo('Popup', ' Error rango semestre')                    
                        else: 
                            messagebox.showinfo('Popup', ' Error en rangos de Obligatorio ')

    def Imprimir(self):
        pass
        # for Subjets in self.listaCursos:
        #     Subjets.getCurso()
            
        # print("Cursos " + str(len(self.listaCursos)))
            # a += 1
            # print(linea , a )
    
            
    def get_listacursos(self):
       
        
        for Subjets in self.listaCursos:
            return str(Subjets.get_codigo())


    




    def get_codig(self):
        
            Subjets.get_codigo()
            
            # print('codigos: ', str((self.listaCursos)))
            
    def longitud_lista(self):
        q= int(len(self.listaCursos))
        return q

    def lista(self):
        return self.listaCursos

        
        