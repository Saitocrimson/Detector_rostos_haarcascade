from tkinter import *
from tkinter import ttk
from  tkinter import tix
from  tkinter import messagebox
from  Camera_funcoes import Camera_funcoes
from Funcoes_principal import Funcoes_principal



root=tix.Tk()

class Detector_camera(Funcoes_principal,Camera_funcoes):
    def __init__(self):
        self.root=root
        self.Principal_Janela()
        self.Label_camera()
        self.Btn_camera()
        root.mainloop()
        
        
    def Principal_Janela(self):
        self.root.title("Detectar Rosto")
        self.root.configure(background='#f2c8f7')
        self.root.geometry('400x400')
        self.root.resizable(False,False)
       

    
    def Label_camera(self):
        self.nomevideo=Label(self.root,bg='#120201')
        self.nomevideo.place(relx=0.1,rely=0.04,relwidth=0.8,relheight=0.6)
        self.nome_foto=""

    def Btn_camera(self):
       
        #ligar camera
        self.btn_liga=Button(self.root,text='ligar',bd=2,bg='#9462bd',fg='white',font=('verdana',8,'bold'),command=self.ligar_camera)
        self.btn_liga.place(relx=0.3,rely=0.7,relwidth = 0.2,relheight=0.1)
        
        #desligar
        self.btn_desligar=Button(self.root,text='desligar',bd=2,bg='#9462bd',fg='white',font=('verdana',8,'bold'),command=self.desligar_camera)
        self.btn_desligar.place(relx=0.5,rely=0.7,relwidth = 0.2,relheight=0.1)
        self.btn_desligar.config(state='disable')



        
Detector_camera()
