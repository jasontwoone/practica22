from tkinter import *
from tkmacosx import Button 
from setuptools import Command
import tkinter.font as font
from a import *
from VAgregar_Curso import *
from VEditar_Curso import *
from VEliminar_curso import *


class Gestionar_cursos:
    def __init__(self):
        pass
    
    def ventanaGestor():

        root = Tk()
        root.title('Gestionar Cursos')
        root.geometry('650x900')

        frame = Frame(root, pady=40, padx=40)
        frame.pack(padx=5, pady=5)

        l0 = Label(frame, text='Gestionar Cursos', font =("Bahnschrift",44)).pack(pady=20)


        btn1 = Button(frame, text = 'Listar Cursos', font =("Bahnschrift",20), fg='#fff', background='#666', width=270,height=4, command= lambda: a.a1()).pack()
        btn2 = Button(frame, text = 'Agregar Curso', font =("Bahnschrift",20),fg='#fff', background='#666', width=270,height=4, command = lambda: ventanaAgregarcurso.ventana() ).pack()
        btn3 = Button(frame, text = 'Editar Curso', font =("Bahnschrift",20),fg='#fff', background='#666', width=270, height=4, command= lambda: ventanaEditar_curso.ventana()).pack()
        btn4 = Button(frame, text = 'Eliminar curso', font =("Bahnschrift",20),fg='#fff', background='#666', width=270, height=4, command= lambda : ventanaEliminarCurso.ventana()).pack()
        btn5 = Button(frame, text = 'Regresar', font =("Bahnschrift",20),fg='#fff', background='#666', width=270, height=4, command = root.destroy).pack()

       
            

        root.mainloop()

        
            