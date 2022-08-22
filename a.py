from ast import Sub
from tkinter import *
from tkinter import ttk
from PIL  import ImageTk, Image
from analizador import *
from Subjects import *
from botones import *

class a:
    def __init__(self):
        pass
        

    def a1():


        top = Toplevel()
        top.title('reporte')
        

        tree = ttk.Treeview(top, height = 20 ,selectmode='extended')
        tree['columns'] = ('Codigo', 'Nombre', 'Prerequisitos','Opcionalidad','Semestre', 'Creditos','Estado')

        tree.column('#0', width=0, stretch=NO)
        tree.column('Codigo')
        tree.column('Nombre')
        tree.column('Prerequisitos')
        tree.column('Opcionalidad')
        tree.column('Semestre')
        tree.column('Creditos')
        tree.column('Estado')

        tree.heading('#0', text='id')
        tree.heading('Codigo', text='Codigo')
        tree.heading('Nombre', text='Nombre')
        tree.heading('Prerequisitos', text='Prerequisitos')
        tree.heading('Opcionalidad', text='Opcionalidad')
        tree.heading('Semestre', text='Semestre')
        tree.heading('Creditos', text='Creditos')
        tree.heading('Estado', text='Estado')

        tree.grid(row=0, column=0)
        

        
        # for Subjets in range(botones.longi()):
        #     tree.insert('', END, Subjets, values=(str(botones.codigos()), 'dos', 'tres','cuatro','cinco','seis','siete'), text='chanchito feliz')
        #     print(str(botones.codigos()))


        #devolver lista

        a = botones.listaB()


        for Subjets in a:
            tree.insert('', END, Subjets, values=(str(Subjets.get_codigo()), Subjets.get_nombre(), Subjets.get_prerrequisito() ,Subjets.get_obligatorio() ,Subjets.get_semestre()  ,Subjets.get_creditos(),  Subjets.get_estado()), text='chanchito feliz')
            # print(str(botones.codigos()))


        # tree.insert('', END, 'lele', values=('cuatro', 'cinco', 'seis'), text='chanchito triste')
        # tree.insert('lele', END, 'lili', values=('4', '5', '6'), text='hijo')

        
        # print('Resultados son ########################')
        # botones.codigos()
        # print(botones.longi())
        
        
        # a = AnalizadorLexico.get_listacursos(Subjets.get_codigo)
        # print(a)

        # Subjets.get_codigo(self)
        
        # botones.
        
        # botones.codigos()


        top.mainloop()