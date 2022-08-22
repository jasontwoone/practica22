from email.mime import text
from tkinter import *
from distutils.cmd import Command
from tkinter import messagebox
from botones import *
from Subjects import *
import tkinter.font as font



class ventanaEliminarCurso():
    def __init__(self):
        pass
     
    
    global e_codigo
    def ventana():

        root = Tk()
        root.title('Eliminar')
        root.geometry('500x300')

        a = botones.listaB()

        

        frame=Frame(root,  padx=10, pady=10, borderwidth=10)
        frame.pack(padx=1, pady=10)

        l1 = Label(frame, text='Eliminar', font =("Bahnschrift",35))
        l1.grid(row=0, column=0, columnspan=1 ,padx=10, pady=10, sticky='w')

        l2 = Label(frame, text='Codigo de Curso: ', font =("Bahnschrift",17))
        l2.grid(row=1, column=0, padx=3, pady=10, sticky='w')


        e_codigo = Entry(frame,  width = 20 ,font =("Bahnschrift",17))
        e_codigo.grid(row=1, column=1, pady=10)
        e_codigo.insert(0, 'Ingrese codigo a eliminar')
  
        def eliminar():
            codigo = e_codigo.get()

            for Subjets in a:
                if Subjets.get_codigo() == codigo:
                    a.remove(Subjets)
                    messagebox.showinfo('Popup', ' Curso eliminado Correctamente')
                    e_codigo.delete(0,END)

        btn1 = Button(frame, text = 'Eliminar', fg='#fff', background='#666', width=8, height=2, command = eliminar )
        btn1.grid(row=2, column=0,pady= 30 , padx= 2)

        btn2 = Button(frame, text = 'Regresar', fg='#fff', background='#666', width=8, height=2, command = root.destroy )
        btn2.grid(row=2, column=1,pady= 30 ,  padx= 1)


        root.mainloop()


