from ast import Sub
from email.mime import text
from tkinter import *
from distutils.cmd import Command
from Subjects import *
from botones import *
import tkinter.font as font



class ventanaEditar_curso():
    def __init__(self):
        pass
     

    
    global e_codigo
    def ventana():

        root = Tk()
        root.title('Hola mundo')
        root.geometry('720x600')

        


        frame = Frame(root, padx=30, pady=30)
        frame.pack(padx=5, pady=5)

      
        
        a = botones.listaB()
        
        l0 = Label(frame, text='Editar ',font =("Bahnschrift",44)).grid(row=0,column=0, columnspan=2,pady=20)
        l1 = Label(frame, text='Codigo:', font =("Bahnschrift",20)).grid(row=1,column=0, sticky='w', padx= 25)
        l2 = Label(frame, text='Nombre:', font =("Bahnschrift",20)).grid(row=2,column=0, sticky='w', padx= 25)
        l3 = Label(frame, text='Pre Requisito:',font =("Bahnschrift",20)).grid(row=3,column=0, sticky='w', padx= 25)
        l4 = Label(frame, text='obligatorio:',font =("Bahnschrift",20)).grid(row=4,column=0, sticky='w', padx= 25)
        l5 = Label(frame, text='semestre:',font =("Bahnschrift",20)).grid(row=5,column=0, sticky='w', padx= 25)
        l6 = Label(frame, text='Creditos:',font =("Bahnschrift",20)).grid(row=6,column=0, sticky='w', padx= 25)
        l7 = Label(frame, text='Estado:',font =("Bahnschrift",20)).grid(row=7,column=0, sticky='w', padx= 25)

        e_codigo = Entry(frame,  width = 40 )
        e_nombre = Entry(frame, width = 40)
        e_prerrequisito = Entry(frame, width = 40)
        e_obligatorio = Entry(frame, width = 40)
        e_semestre = Entry(frame, width = 40)
        e_creditos = Entry(frame, width = 40)
        e_estado = Entry(frame, width = 40)

        e_codigo.grid(row=1,column=1)
        e_nombre.grid(row=2,column=1)
        e_prerrequisito.grid(row=3,column=1)
        e_obligatorio.grid(row=5,column=1)
        e_semestre.grid(row=4,column=1)
        e_creditos.grid(row=6,column=1)
        e_estado.grid(row=7,column=1)
        
        def click():
            codigo = e_codigo.get()
          
            nombre = e_nombre.get()
            prerequisito = e_prerrequisito.get()
            obligatorio = e_obligatorio.get()
            semestre = e_semestre.get()
            creditos = e_creditos.get()
            estado = e_estado.get()

            index = 0

            for Subjets in a:
                if Subjets.get_codigo() == codigo:
                    # print('encontrado')
                    # e_codigo.insert(0, Subjets.get_codigo())
                    e_nombre.insert(0, Subjets.get_nombre())
                    e_prerrequisito.insert(0, Subjets.get_prerrequisito())
                    e_obligatorio.insert(0, Subjets.get_obligatorio())
                    e_semestre.insert(0, Subjets.get_semestre())
                    e_creditos.insert(0, Subjets.get_creditos())
                    e_estado.insert(0, Subjets.get_estado())
                    # print('Codigo', Subjets.get_codigo(), 'nombre: ', Subjets.get_nombre())
                    
                index +=1


        def click_editar():
            codigo = e_codigo.get()
            copia_codigo = codigo
            nombre = e_nombre.get()
            prerequisito = e_prerrequisito.get()
            obligatorio = e_obligatorio.get()
            semestre = e_semestre.get()
            creditos = e_creditos.get()
            estado = e_estado.get()
            
            editado = False
            
            for Subjets in a:
                
                if Subjets.get_codigo() == codigo:
                    
                    Subjets.set_nombre(nombre)
                    Subjets.set_prerrequisito(prerequisito)
                    Subjets.set_obligatorio(obligatorio)
                    Subjets.set_semestre(semestre)
                    Subjets.set_creditos(creditos)
                    Subjets.set_estado(estado)
                    

                    editado = True
                    limpiar_Campos()
            
            if editado == False:
                pass
                # llenar(codigo, nombre, prerequisito, obligatorio, semestre, creditos, estado, copia_codigo )
                
        def limpiar_Campos():
            e_codigo.delete(0, END)
            e_nombre.delete(0, END)
            e_prerrequisito.delete(0, END)
            e_obligatorio.delete(0, END)
            e_semestre.delete(0, END)
            e_creditos.delete(0, END)
            e_estado.delete(0, END)
               
            e_codigo.delete(0, END)
           
        btn1 = Button(frame, text = 'Buscar codigo', fg='#fff', background='#666', width=20, height=7, command = click )
        btn2 = Button(frame, text = 'Editar', fg='#fff', background='#666', width=20, height=7, command =  click_editar )
        btn1.grid(row=8,column=0, pady= 30 , padx= 25)
        btn2.grid(row=8,column=1,pady= 30 , padx= 10)
