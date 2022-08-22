from tkinter import *
from webbrowser import MacOSX
from tkmacosx import Button
from tkinter.ttk import Sizegrip
from turtle import bgcolor, left
from pyparsing import col
from setuptools import Command
from botones import botones
from VGestionar_cursos import *
from VConteo_Creditos import *
import tkinter.font as font



class ventanaPrincipal:
    def __init__(self):

        pass



    def ventana():
        root = Tk()
        root.title('Practica 1')
        
    
        root.geometry('650x800')


        frame = LabelFrame(root, text= ' Datos', padx=20, pady=20)
        frame.pack(padx=5, pady=5, )

        l1 = Label(frame, text='Nombre de curso:       Lab Lenguajes formales y de programacion').pack(anchor=NW)
        l2 = Label(frame, text='Nombre estudiante:   Jason Neftali Castañeda Roca').pack(anchor=NW)
        l3 = Label(frame, text='Carné estudiante:    201700460').pack(anchor=NW)

        frame2 = Frame(root, pady=2, padx=2)
        frame2.pack(padx=40, pady=40)

        l0 = Label(frame2, text='Menu', font =("Bahnschrift",44)).pack(pady=18)

 
        btn1 = Button(frame2, text = 'Cargar Archivo', bg='orange',fg='#fff',font =("Bahnschrift",20),   width=200, height=4,command= lambda: botones.boton_cargarArchivo())
        btn1.pack()
        btn2 = Button(frame2, text = 'Gestionar Cursos', font =("Bahnschrift",20),fg='#fff', background='#004', width=200,height=4,  command= lambda: Gestionar_cursos.ventanaGestor()).pack()
        btn3 = Button(frame2, text = 'Conteo de Creditos', font =("Bahnschrift",20), fg='#fff', bg='orange', width=200,height=4, command= lambda : ventanaConteoCreditos.ventana()).pack()
        btn4 = Button(frame2, text = 'Salir', fg='#fff',font =("Bahnschrift",20),background='#666', width=200, height=4, command= root.destroy).pack()
        

        root.mainloop()
