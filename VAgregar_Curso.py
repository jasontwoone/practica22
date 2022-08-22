from email.mime import text
from tkinter import *
from distutils.cmd import Command
import tkinter.font as font
from tkinter import messagebox
from botones import *
from Subjects import *



class ventanaAgregarcurso():
    def __init__(self):
        pass
     
    
    global e_codigo
    def ventana():

        root = Tk()
        root.title('Agegar Curso')
        root.geometry('750x600')

        a = botones.listaB()

        frame = Frame(root, padx=30, pady=30)
        frame.pack(padx=5, pady=5)
        

        l0 = Label(frame, text='Ingresar Datos', font =("Bahnschrift",44)).grid(row=0,column=0, columnspan=2, pady=20)
        l1 = Label(frame, text='Codigo:', font =("Bahnschrift",20)).grid(row=1,column=0, sticky='w', padx= 25)
        l2 = Label(frame, text='Nombre:' , font =("Bahnschrift",20)).grid(row=2,column=0,sticky='w', padx= 25)
        l3 = Label(frame, text='Pre Requisito:', font =("Bahnschrift",20)).grid(row=3,column=0,sticky='w', padx= 25)
        l4 = Label(frame, text='semestre:', font =("Bahnschrift",20)).grid(row=4,column=0,sticky='w', padx= 25)
        l5 = Label(frame, text='obligatorio:', font =("Bahnschrift",20)).grid(row=5,column=0,sticky='w', padx= 25)
        l6 = Label(frame, text='Creditos:', font =("Bahnschrift",20)).grid(row=6,column=0,sticky='w', padx= 25)
        l7 = Label(frame, text='Estado:', font =("Bahnschrift",20)).grid(row=7,column=0,sticky='w', padx= 25)

        e_codigo = Entry(frame,  width = 40 )
        e_nombre = Entry(frame, width = 40)
        e_prerrequisito = Entry(frame, width = 40)
        e_obligatorio = Entry(frame, width = 40)
        e_semestre = Entry(frame, width = 40)
        e_creditos = Entry(frame, width = 40)
        e_estado = Entry(frame, width = 40)

        e_codigo.grid(row=1,column=1,sticky='nswe')
        e_nombre.grid(row=2,column=1,sticky='nswe')
        e_prerrequisito.grid(row=3,column=1,sticky='nswe')
        e_obligatorio.grid(row=5,column=1,sticky='nswe')
        e_semestre.grid(row=4,column=1,sticky='nswe')
        e_creditos.grid(row=6,column=1,sticky='nswe')
        e_estado.grid(row=7,column=1,sticky='nswe')
        
        def click():
            codigo = e_codigo.get()
            nombre = e_nombre.get()
            prerequisito = e_prerrequisito.get()
            obligatorio = e_obligatorio.get()
            semestre = e_semestre.get()
            creditos = e_creditos.get()
            estado = e_estado.get()
            
            longitud = len(prerequisito)
            contador = 0
            es = 0
            
            # if prerequisito is not None:
            #     es = 1
                
            #     print('antes ',prerequisito)
            #     prerequisito = '1'
            #     print('despues ',prerequisito)
                




            if codigo != ''and nombre != '' and obligatorio != '' and semestre != '' and creditos != "" and estado != '' :
                if codigo.isnumeric() and  semestre.isnumeric() and creditos.isnumeric():
                    
            
                # primera parte 
                    for letra in prerequisito:
                        if letra.isnumeric() or letra == ';' or letra.isspace():
                            contador += 1

                            if contador == longitud:
                                

                                # if es == 1:
                                #     prerequisito = ""

                                # vaciar 

                                if obligatorio == '0' or obligatorio =='1':

                                    if estado == '0' or estado == '1' or estado == '-1':

                                        if int(semestre) >= 1 and int(semestre)<=10:

                                            if  int(creditos) >= 0:


                                                a.append(Subjets(codigo,nombre,prerequisito,obligatorio,semestre,creditos,estado))
                                                limpiar()
                                            else: 
                                                messagebox.showinfo('Popup', 'Error Campo creditos')

                                            messagebox.showinfo('Popup', ' Curso Agregado')
                                        else: 
                                            messagebox.showinfo('Popup', ' Rango "Semestre" Incorrrecto (1-10)')
                                    else:
                                        messagebox.showinfo('Popup', ' Rango "Estado" Incorrecto (-1,0,1)' )

                                else: 
                                    messagebox.showinfo('Popup', 'Rango "obligatorio" Incorrecto (0,1)')

                        else:
                            messagebox.showinfo('Popup', ' Simbolo desconocido en prerequisitos: ' )

                
                            break
                else: 
                    messagebox.showinfo('Popup', ' Campos: digito, obligatorio, semestre, creditos, estado son numericos' )
            else: 
                messagebox.showinfo('Popup', ' Campos vacios aexcepción de prerequisitos ' )

    
            

            

            # print(codigo)
            # print(nombre)
            # print(prerequisito)
            # print(obligatorio)
            # print(semestre)
            # print(creditos)
            # print(estado)
            # l = Label(root ,text=texto)
            # l.pack()
            # e_codigo.delete(0, END)
            # l.configure(text=texto)


        btn1 = Button(frame, text = 'Agregar' , font =("Bahnschrift",20), fg='#fff', background='#666', width=15, height=4, command = click )
        btn1.grid(row=8,column=1, pady= 30 , padx= 10)
        btn2 = Button(frame, text = 'Regresar', font =("Bahnschrift",20),fg='#fff', background='#666', width=15, height=4, command = root.destroy )
        btn2.grid(row=8,column=0, pady= 30 , padx= 25)

      
        
        def limpiar():
            e_codigo.delete(0, END)
            e_nombre.delete(0, END)
            e_prerrequisito.delete(0, END)
            e_obligatorio.delete(0, END)
            e_semestre.delete(0, END)
            e_creditos.delete(0, END)
            e_estado.delete(0, END)
            e_codigo.delete(0, END)
            
        root.mainloop()

    

    
