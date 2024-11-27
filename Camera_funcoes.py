import cv2
import time
from tkinter import *
from tkinter import ttk
from  tkinter import tix
from PIL import Image,ImageTk



class Camera_funcoes():
    def iniciar_camera(self):
        global video
        xml_haarcascade='haarcascade_frontalface_alt2.xml'
        self.face_classificador=cv2.CascadeClassifier(xml_haarcascade)
        video=cv2.VideoCapture(0)
        #tamanho da resolução da camera
        video.set(3,320)
        video.set(4,240)
        print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        self.liga_camera()
        
    def liga_camera(self):
        global video
        ret,frame=video.read()
        if ret==True:
            #configuracao visibilidade dos botoes 
            self.btn_liga.config(state='disable')
            self.btn_desligar.config(state='normal')
            
            #captura a imagem
            frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            #reconhece a face
            faces = self.face_classificador.detectMultiScale(frame)
            for (x,y,largura,altura) in faces:
                cv2.rectangle(frame,(x,y),(x+largura,y+altura),(0,0,255),2)
                
            #converte para pil
            img=Image.fromarray(frame)
            #pconverte para imagem tkinter
            image=ImageTk.PhotoImage(image=img)
            #associa a janela
            self.nomevideo.configure(image=image)
            #associa a imagem coma a label
            self.nomevideo.image=image
            #mantem a camera funcionando
            self.nomevideo.after(10,self.liga_camera)
           
                            
        else:
            print("deu ruim")
    
    def sair(self):
        global video
        video.release()
        self.nomevideo.config(image='')
        self.nomevideo.configure(bg = "#120201")
        self.btn_liga.config(state='normal')
        self.btn_desligar.config(state='disable')
        
