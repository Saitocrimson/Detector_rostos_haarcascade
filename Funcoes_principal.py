class Funcoes_principal():
    def ligar_camera(self):
        #configuracao visibilidade dos botoes 
        self.btn_liga.config(state='disable')
        self.btn_desligar.config(state='normal')
        self.iniciar_camera()
              

      
    def desligar_camera(self):
        self.sair()
        self.nomevideo.config(image='')
        self.nomevideo.configure(bg = "#120201")
        self.btn_liga.config(state='normal')
        self.btn_desligar.config(state='disable')
