from email.mime import text
from re import sub
from sqlite3 import Row
import string
from tkinter import *
from distutils.cmd import Command



from botones import *
from Subjects import *



class ventanaConteoCreditos():
    def __init__(self):
        pass
     
    
    global e_codigo
    def ventana():

        root = Tk()
        root.title('Conteo de Creditos')
        root.geometry('700x700')
        a = botones.listaB()
        

        frame = Frame(root, padx=30, pady=30)
        frame.pack(padx=5, pady=5)

        frame2 = Frame(root, padx=30, pady=30)
        frame2.pack(padx=5, pady=5)

        frame3 = Frame(root, padx=30, pady=30)
        frame3.pack(padx=5, pady=5)

        l0 = Label(frame, text='Conteo de Creditos', font =("Bahnschrift",44)).grid(row=0,column=0, columnspan=2, pady=20)


        def Creditos_until_N():
            creditosN = 0
            for Subjets in a:
                if int(Subjets.get_obligatorio()) == 1 and int(Subjets.get_semestre()) <= int(value1.get()):
                    creditosN += int(Subjets.get_creditos())
            e_semestre_N1.insert(0, creditosN)
            
        def creditos_SemestreN():
            creditosAP = 0
            for Subjets in a:
                if Subjets.get_semestre() == value2.get() and int(Subjets.get_estado()) == 0:
                    print('valor del value: ', value2.get() )
                    creditosAP += int(Subjets.get_creditos())
                    print('CReditos aprobados' , creditosAP)

            print('CReditos aprobados total ' , creditosAP)
                    
            e_creditos_Aprobados_semestre.insert(0,creditosAP)


            creditosASIG = 0
            for Subjets in a:
                if Subjets.get_semestre() == value2.get() and int(Subjets.get_estado()) ==1:
                    creditosASIG += int(Subjets.get_creditos())
            e_creditos_Asignados_semestre.insert(0, creditosASIG)

            creditosPEND = 0
            
            for Subjets in a:
                if Subjets.get_semestre() == value2.get() and int(Subjets.get_estado()) ==-1:
                    creditosPEND += int(Subjets.get_creditos())
            e_creditos_Pendientes_semestre.insert(0, creditosPEND)

            


        lista_semestres=[1,2,3,4,5,6,7,8,9,10]
        
        value1 = StringVar()
        value1.set(lista_semestres[0])

        value2 = StringVar()
        value2.set(lista_semestres[0])

        drop1 = OptionMenu(frame2, value1, *lista_semestres)
        drop1.grid(row=5,column=1)

        drop2 = OptionMenu(frame3, value2, *lista_semestres)
        drop2.grid(row=9,column=1)
        
        
        creditos_aprobados = 0
        creditos_Cursando = 0
        creditos_pendientes= 0
        #Conteo de cursos aprovados
        creditos = 0
        for Subjets in a:
            if int(Subjets.get_estado()) == 0:
                creditos += int(Subjets.get_creditos())
                creditos_aprobados = creditos
                
                    
        creditos2 = 0
        for Subjets in a:
            if int(Subjets.get_estado()) == 1:
                creditos2 += int(Subjets.get_creditos())
                creditos_Cursando = creditos2
                
        
        creditos3 = 0
        for Subjets in a:
            if int(Subjets.get_estado()) == -1 and int(Subjets.get_obligatorio()) == 1:
                creditos3 += int(Subjets.get_creditos())
                creditos_pendientes = creditos3
                

        
            
        
        
        
        
        
        # l0 = Label(root, text='Creditos Aprobados').grid(row=0,column=0, columnspan=2)
        l0 = Label(frame, text='Creditos Aprobados:', font =("Bahnschrift",15)).grid(row=1,column=0)
        L_CreditosAprobados=Label(frame, text=creditos_aprobados,font =("Bahnschrift",15)).grid(row = 1, column=1)
        l1 = Label(frame, text='Creditos Cursando:',font =("Bahnschrift",15)).grid(row=2,column=0)
        L_CreditosCursando=Label(frame, text=creditos_Cursando,font =("Bahnschrift",15)).grid(row = 2, column=1)
        l2 = Label(frame, text='Creditos Pendientes:',font =("Bahnschrift",15)).grid(row=3,column=0)
        L_CreditosPendientes=Label(frame, text=creditos_pendientes,font =("Bahnschrift",15)).grid(row = 3, column=1)
        
        l3 = Label(frame2, text='Creditos Obligatorios: ',font =("Bahnschrift",15)).grid(row=4,column=0,sticky= 'w')
        l4 = Label(frame2, text='Semestre',font =("Bahnschrift",15)).grid(row=5,column=0, sticky= 'e')
        value = StringVar()
        value.set('1')

        

        l5 = Label(frame3, text='Creditos aprobados Semestre:',font =("Bahnschrift",15)).grid(row=6,column=0, sticky= 'w')
        l5 = Label(frame3, text='Creditos asignados Semestre:',font =("Bahnschrift",15)).grid(row=7,column=0, sticky= 'w')
        l5 = Label(frame3, text='Creditos pendientes Semestre:',font =("Bahnschrift",15)).grid(row=8,column=0, sticky= 'w')


        l6 = Label(frame3, text='Semestre', font =("Bahnschrift",15)).grid(row=9,column=0, sticky= 'e')
        
        e_semestre_N1 = Entry(frame2 )
        e_creditos_Aprobados_semestre = Entry(frame3 )
        e_creditos_Asignados_semestre = Entry(frame3 )
        e_creditos_Pendientes_semestre = Entry(frame3 )
       
        e_semestre_N1.grid(row=4,column=1)
        e_creditos_Aprobados_semestre.grid(row=6,column=1)
        e_creditos_Asignados_semestre.grid(row=7,column=1)
        e_creditos_Pendientes_semestre.grid(row=8,column=1)

       
        def limpiar():
            e_semestre_N1.delete(0,END)
            e_creditos_Aprobados_semestre.delete(0, END)
            e_creditos_Asignados_semestre.delete(0, END)
            e_creditos_Pendientes_semestre.delete(0,END)

        

        
        
        
            
            

        btn1 = Button(frame2, text = 'Contar', fg='#fff', background='#666', width=5 ,height=3, command= Creditos_until_N)
        btn1.grid(row=4, rowspan = 2, column=2, padx=5)

        btn2 = Button(frame3, text = 'Contar', fg='#fff', background='#666', width=5, height=5, command= creditos_SemestreN )
        btn2.grid(row=6,column=2,   rowspan= 3 , padx=5)

        btn3 = Button(frame3, text = 'Limpiar Datos', fg='#fff', background='#666', width=12 ,height='5',  command = limpiar )
        btn3.grid(row=10,column=2)


        root.mainloop()