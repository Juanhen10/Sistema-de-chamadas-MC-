'''
Apicativo de chamadas 
proporção 
height=400
width = 450 
center height = 200
center width = 225

lembrando que é largura(width) primeiro de depois altura (height)
'''

from pathlib import Path

from PIL import Image, ImageTk

import tkinter as tk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys
from utils import IMAGEM_DIR, PlaceholderEntry
import pyttsx3
# Nome das telas
class Main_Window:
    def __init__(self, window):
        # Sistema de voz
        self.engine = pyttsx3.init()
        # Criando o a tela #
        self.window = window
        self.window.configure(bg="#BB9753")
        self.tela = tk.Canvas(
            window,
            bg="#BB9753",
            height=400,
            width=450,
            relief="ridge"
        )
        self.tela.place(x = 0, y = 0)
        self.tela.pack()
        
        # adicionando imagem de home
        self.home_imagem = PhotoImage(
            file= IMAGEM_DIR /"image_1.png")
        self.tela.create_image(
            230.0,
            205.0,
            image=self.home_imagem
        )

        ''' OUTRAS IMAGENS '''
        # logo imagem
        self.logo_imagem = PhotoImage(
            file = IMAGEM_DIR / "logo_ofner.png" 
        )
        self.tela.create_image(
            70,
            350,
            image=self.logo_imagem
        )
        # painel imagem
        self.painel_imagem = PhotoImage(
            file= IMAGEM_DIR / 'tema.png'
        )
        self.tela.create_image(
            225.5,
            100,
            image= self.painel_imagem
        )
        # Lista de chamados
        self.calls = []
        # configurando o Botões 
        self.btn_imagem = PhotoImage(
        file= IMAGEM_DIR / "button_1.png"
    )
        self.btn_call = Button(
            relief="raised",
            cursor= "mouse",
            activebackground= "white",
            bg= "#ffffff",
            image=self.btn_imagem,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_call,
            
            )
        self.btn_call.place(
            x=160.0,
            y=217,
            width=120.0,
            height=45.0
        )

        # Criando input de texto
        self.input_bkg = PhotoImage(
            file= IMAGEM_DIR / 'entry_1.png'
        )
        self.tela.create_image(
            228.25,
            201.5,
            image=self.input_bkg
        )
        self.input = PlaceholderEntry(
            window,
            placeholder="Digite senha ou nome",
            bg="#BB9753",
            fg="#000716",
            font="Lalezar",
            justify="center",
            bd=0   
        )
        self.style_entry()
        self.input.place(
            x=115,
            y=185.8,
            width=226.5,
            height=25.0
        )
        self.input.lift()
        # visualizador dos nomes chamados | não chamados
        
        self.screen_btn_bg = PhotoImage(
            file= IMAGEM_DIR / 'verificando (1).png'
        )
        self.tela.create_image(
            400,
            350,
            image = self.screen_btn_bg
        )
        
        self.screen_btn = tk.Button(
            window,
            cursor= 'hand2',
            bg="#FFFFFF",
            command=self.open_second_window,
            image= self.screen_btn_bg,
            borderwidth=0,
            highlightthickness=0,

        )
        self.screen_btn.place(x=380, y=333, width=35, height=35)
        # registrando o nome
        self.calls_var = tk.StringVar(value=self.calls)
    
    def add_call(self, event=None):
        call = self.input.get().strip()
        if call:
            self.calls.insert(0, call)
            if len(self.calls) > 5:
                self.calls.pop()
            self.calls_var.set(self.calls)
            self.input.delete(0, tk.END)
            self.announce_call(call)
    def announce_call(self, call):
        self.engine.say(call)
        self.engine.runAndWait()

    # Configuração da tela de visualização 
    def open_second_window(self):
        self.second_window = tk.Toplevel(self.window)
        self.second_window.title("Nomes e Senhas")
        self.second_window.configure(bg="#BB9753" )
        self.second_window.geometry("800x600")
        self.second_window.resizable(False, False)
        # Frame de titulo 1 
        frame = tk.Frame(self.second_window, bg='white')
        frame.pack(pady=10, anchor="sw", padx=100)
        title = tk.Label(frame, text="Nomes aguardando", 
                                font=("Arial", 20),
                                bg="#BB9753",
                                fg="#ffffff")
        title.pack()
        # LOGO 
        logo_image = PhotoImage(file= IMAGEM_DIR / "logo_ofner.png")
        logo_label = tk.Label(frame,image=logo_image, bg="#BB9753")
        logo_label.image = logo_image
        logo_label.pack(pady=20) 
        # Colocando o design e chamando os nome na segunda tela
        self.calls = []
        self.calls_var = tk.StringVar(value=self.calls)
        self.calls_listbox = tk.Listbox(
            self.second_window, 
            listvariable=self.calls_var,
            font=("Arial",30), 
            height=50,
            width=21,
            fg="red"
            )
        self.calls_listbox.pack(anchor="sw", pady=10, padx=5)
       # Nomes chamados 
       

     # Configurando o logotipo na segunda janela
           
      
        
        
        
    def make_window_transparent(self, alpha):
        self.window.attributes("-alpha", alpha)
        
    def style_entry(self): # type: ignore
        self.input.configure(highlightthickness=0.5, borderwidth=0.6)
        # Adiciona o Canvas à janela principal

    def style_entry(self):
        self.input.configure(highlightthickness=0.5, borderwidth=0.6)




if __name__ == "__main__":
    wd = tk.Tk()
    app = Main_Window(wd)
    wd.resizable(False,False)
    wd.mainloop()
    ###############
    
    