from tkinter import *
from tkinter import filedialog
from analizador import AnalizadorLexico

class botones():
    global objeto
    objeto = AnalizadorLexico()
    def __init__(self,ruta):
        self.ruta =ruta
        
        pass

    def boton_cargarArchivo():
        # top = Toplevel()
        # top.title("Cargar Archivo")
        filename = filedialog.askopenfilename(title='Elige un archivo LFP', filetypes=(("Archivos PNG",".lfp"),('todos','*'))) 
        texto = open (filename)
        contenido = texto.readlines()
        
       
        
        
        objeto.analizador(contenido)
        objeto.Imprimir()
        
        
        

        # top.mainloop()  
        #print(root.filename)
          
    def codigos():
        a = objeto.get_listacursos()
        return a

    def longi():
        a = objeto.longitud_lista()
        return a

    def listaB():
        a = objeto.lista()
        return a

    
        
       
       
        
    

