import tkinter as tk
from tkinter import font as tkfont
import subprocess as sb

class RetroTech:
    def __init__(self, root):
        self.root = root
        self.root.title("RetroTech")
        self.root.geometry("600x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E2E2E")
        

        self.fonte_titulo = tkfont.Font(family="Courier New", size=24, weight="bold")
        self.fonte_botao = tkfont.Font(family="Courier New", size=14, weight="bold")
        

        self.cor_fundo = "#2E2E2E"
        self.cor_destaque = "#4CAF50"
        self.cor_texto = "#FFFFFF"
        self.cor_botao = "#3A3A3A"
        self.cor_borda = "#1E1E1E"
        

        self.frame_principal = tk.Frame(
            self.root, 
            bg=self.cor_botao,
            bd=3,
            relief=tk.RAISED,
            highlightbackground=self.cor_destaque,
            highlightthickness=2
        )
        self.frame_principal.pack(pady=40, padx=40, fill=tk.BOTH, expand=True)
        

        self.titulo = tk.Label(
            self.frame_principal,
            text="Bem-vindo ao RetroTech",
            font=self.fonte_titulo,
            fg=self.cor_destaque,
            bg=self.cor_botao
        )
        self.titulo.pack(pady=(30, 20))
        
        self.btn_janela1 = tk.Button(
            self.frame_principal,
            text="CLIQUE AQUI",
            command=self.abrir_janela1,
            font=self.fonte_botao,
            fg=self.cor_texto,
            bg=self.cor_botao,
            activebackground=self.cor_destaque,
            activeforeground=self.cor_texto,
            relief=tk.RAISED,
            bd=4,
            padx=20,
            pady=10,
            highlightbackground=self.cor_destaque,
            highlightcolor=self.cor_destaque,
            highlightthickness=2
        )
        self.btn_janela1.pack(pady=20, ipadx=10, ipady=5)
        

        self.rodape = tk.Label(
            self.root,
            text="© 2023 RetroTech Systems | Versão 1.0",
            font=("Courier New", 8),
            fg=self.cor_destaque,
            bg=self.cor_fundo
        )
        self.rodape.pack(side=tk.BOTTOM, pady=10)
    
    def abrir_janela1(self):
        """Abre a janela secundária"""
        sb.Popen(["python", "janela1.py"])

if __name__ == "__main__":
    root = tk.Tk()
    app = RetroTech(root)
    root.mainloop()