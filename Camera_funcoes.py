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
           
            
            #captura a imagem
            frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #cria texto em cima da imagem da webcam
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,"centralize o rosto ",(10,20), font, 1, (200,255,0), 3,2)
            cv2.putText(frame,"+",(150,130), font, 1, (0,255,255), 4,1)
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
        
        
