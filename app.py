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

import tkinter as tk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys
from utils import IMAGEM_DIR

# Nome das telas
class Visualização_screen:
      def __init__(self, window):
        # Criando o a tela #
        self.window = window
        self.window.configure(bg="#BB9753")
        self.visualizar = tk.Canvas(
            window,
            bg="#BB9753",
            height=400,
            width=450,
            relief="ridge"
        )
        self.visualizar.place(x = 0, y = 0)
        self.visualizar.pack()

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = "black"
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self.focus_in_event)
        self.bind("<FocusOut>", self.focus_out_event)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color
    
    def focus_in_event(self, event):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self["fg"] = self.default_fg_color
    
    def focus_out_event(self, event):
        if not self.get():
            self.put_placeholder()
            self["fg"] = self.placeholder_color


class Main_Window:
    def __init__(self, window):
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
            command=lambda: print('botão clicado'),
            
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
        print(self.input)
        
        # Notoficação de registro
        
        self.notify_img = PhotoImage(
            file= IMAGEM_DIR / 'image_3.png'
            )
    
        self.tela.create_image(
            226.0,
            333.0,
            image=self.notify_img
                )
    
        self.button = tk.Button(
            window,
            text="Abrir segunda tela",
            command=self.open_second_window,
            bg="#BB9753",
            fg="#000716",
            font="Lalezar",
            borderwidth=0,
            highlightthickness=0
        )
        self.button.place(x=115, y=220, width=226.5, height=25.0)

    def open_second_window(self):
        second_window = tk.Toplevel(self.window)
        second_window.title("Nomes e Senhas")
        second_window.configure(
            bg="#BB9753"
        )
        second_window.geometry("450x400")

        tela = tk.Canvas(
            second_window,
            bg ="BB9753",
            height=400,
            width=450,
            relief="ridge"
        )

        tela.place(x=0, y=0)
        tela.pack()

        label = tk.Label(second_window,
                         text="Tela",
                         bg="#BB9753",
                         fg="#000716",
                         font="Lalezar"
                         )
        label.pack(pady=20)
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
    
    