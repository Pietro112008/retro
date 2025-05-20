import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import hashlib
import subprocess as sb
from tkinter import font as tkfont

class SistemaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login Premium")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Configuração de estilos
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 10), padding=6)
        self.style.configure('TLabel', background="#f0f0f0", font=('Helvetica', 10))
        self.style.configure('TEntry', font=('Helvetica', 10))
        
        # Cores personalizadas
        self.cor_principal = "#4a6baf"
        self.cor_secundaria = "#6c8cd5"
        self.cor_texto = "#ffffff"
        self.cor_destaque = "#ff5722"
        
        # Arquivo para armazenar os usuários
        self.arquivo_usuarios = 'usuarios.json'
        
        # Frame principal com sombra visual
        self.frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief=tk.RAISED)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=350, height=200)
        
        # Título estilizado
        self.label_titulo = tk.Label(
            self.frame, 
            text="Sistema Premium", 
            font=('Helvetica', 18, 'bold'), 
            bg="#ffffff", 
            fg=self.cor_principal
        )
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=(20, 15))
        
        # Botões com estilo moderno
        self.btn_cadastro = ttk.Button(
            self.frame, 
            text="Cadastrar", 
            command=self.abrir_janela_cadastro, 
            style='TButton'
        )
        self.btn_cadastro.grid(row=1, column=0, pady=5, padx=10, sticky="ew")
        
        self.btn_login = ttk.Button(
            self.frame, 
            text="Login", 
            command=self.abrir_janela_login, 
            style='TButton'
        )
        self.btn_login.grid(row=1, column=1, pady=5, padx=10, sticky="ew")
        
        # Rodapé
        self.label_rodape = tk.Label(
            self.root, 
            text="© 2023 Sistema Premium - Todos os direitos reservados", 
            font=('Helvetica', 8), 
            bg="#f0f0f0", 
            fg="#666666"
        )
        self.label_rodape.pack(side=tk.BOTTOM, pady=10)
        
        # Carrega os usuários existentes
        self.carregar_usuarios()
    
    def carregar_usuarios(self):
        """Carrega os usuários do arquivo JSON"""
        if os.path.exists(self.arquivo_usuarios):
            with open(self.arquivo_usuarios, 'r') as f:
                try:
                    self.usuarios = json.load(f)
                except json.JSONDecodeError:
                    self.usuarios = {}
        else:
            self.usuarios = {}
    
    def salvar_usuarios(self):
        """Salva os usuários no arquivo JSON"""
        with open(self.arquivo_usuarios, 'w') as f:
            json.dump(self.usuarios, f, indent=4)
    
    def hash_senha(self, senha):
        """Cria um hash da senha para armazenamento seguro"""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def abrir_janela_cadastro(self):
        """Abre a janela de cadastro estilizada"""
        self.janela_cadastro = tk.Toplevel(self.root)
        self.janela_cadastro.title("Cadastro de Usuário")
        self.janela_cadastro.geometry("350x250")
        self.janela_cadastro.resizable(False, False)
        self.janela_cadastro.configure(bg="#ffffff")
        
        # Frame interno
        frame_cadastro = tk.Frame(self.janela_cadastro, bg="#ffffff")
        frame_cadastro.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Título
        tk.Label(
            frame_cadastro, 
            text="Cadastre-se", 
            font=('Helvetica', 14, 'bold'), 
            bg="#ffffff", 
            fg=self.cor_principal
        ).grid(row=0, column=0, columnspan=2, pady=(0, 15))
        
        # Campos de entrada
        ttk.Label(frame_cadastro, text="Nome de usuário:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_usuario_cadastro = ttk.Entry(frame_cadastro)
        self.entry_usuario_cadastro.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Label(frame_cadastro, text="Senha:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_senha_cadastro = ttk.Entry(frame_cadastro, show="*")
        self.entry_senha_cadastro.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Label(frame_cadastro, text="Confirmar senha:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_confirma_senha = ttk.Entry(frame_cadastro, show="*")
        self.entry_confirma_senha.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        # Botão de cadastro com cor destacada
        btn_cadastrar = tk.Button(
            frame_cadastro, 
            text="Cadastrar", 
            command=self.cadastrar_usuario,
            bg=self.cor_principal,
            fg=self.cor_texto,
            font=('Helvetica', 10, 'bold'),
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=5
        )
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=(15, 0))
    
    def cadastrar_usuario(self):
        """Realiza o cadastro de um novo usuário"""
        usuario = self.entry_usuario_cadastro.get()
        senha = self.entry_senha_cadastro.get()
        confirma_senha = self.entry_confirma_senha.get()
        
        if not usuario or not senha:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        if senha != confirma_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return
        
        if usuario in self.usuarios:
            messagebox.showerror("Erro", "Nome de usuário já existe!")
            return
        
        # Armazena o hash da senha
        self.usuarios[usuario] = self.hash_senha(senha)
        self.salvar_usuarios()
        
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        self.janela_cadastro.destroy()
    
    def abrir_janela_login(self):
        """Abre a janela de login estilizada"""
        self.janela_login = tk.Toplevel(self.root)
        self.janela_login.title("Login de Usuário")
        self.janela_login.geometry("350x200")
        self.janela_login.resizable(False, False)
        self.janela_login.configure(bg="#ffffff")
        

        frame_login = tk.Frame(self.janela_login, bg="#ffffff")
        frame_login.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        

        tk.Label(
            frame_login, 
            text="Faça seu Login", 
            font=('Helvetica', 14, 'bold'), 
            bg="#ffffff", 
            fg=self.cor_principal
        ).grid(row=0, column=0, columnspan=2, pady=(0, 15))

        ttk.Label(frame_login, text="Nome de usuário:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_usuario_login = ttk.Entry(frame_login)
        self.entry_usuario_login.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Label(frame_login, text="Senha:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_senha_login = ttk.Entry(frame_login, show="*")
        self.entry_senha_login.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        

        btn_login = tk.Button(
            frame_login, 
            text="Entrar", 
            command=self.fazer_login,
            bg=self.cor_principal,
            fg=self.cor_texto,
            font=('Helvetica', 10, 'bold'),
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=5
        )
        btn_login.grid(row=3, column=0, columnspan=2, pady=(15, 0))
    
    def fazer_login(self):
        """Realiza o login do usuário"""
        usuario = self.entry_usuario_login.get()
        senha = self.entry_senha_login.get()
        
        if not usuario or not senha:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        if usuario not in self.usuarios:
            messagebox.showerror("Erro", "Usuário não encontrado!")
            return
        
        if self.usuarios[usuario] != self.hash_senha(senha):
            messagebox.showerror("Erro", "Senha incorreta!")
            return
        
        messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
        self.janela_login.destroy()
        

        self.abrir_janela_pos_login(usuario)
    
    def abrir_janela2(self):
        """Abre a segunda janela (calendário)"""
        sb.Popen(["python", "janela2.py"])
        
    def abrir_janela_pos_login(self, usuario):
        """Abre a janela pós-login decorada"""
        self.janela_pos_login = tk.Toplevel(self.root)
        self.janela_pos_login.title(f"Bem-vindo - {usuario}")
        self.janela_pos_login.geometry("500x400")
        self.janela_pos_login.configure(bg="#ffffff")
        

        frame_pos_login = tk.Frame(self.janela_pos_login, bg="#ffffff")
        frame_pos_login.pack(pady=30, padx=30, fill=tk.BOTH, expand=True)
        

        tk.Label(
            frame_pos_login, 
            text=f"Olá, {usuario}!", 
            font=('Helvetica', 18, 'bold'), 
            bg="#ffffff", 
            fg=self.cor_principal
        ).pack(pady=(0, 10))
        
        tk.Label(
            frame_pos_login, 
            text="Você está logado no sistema premium", 
            font=('Helvetica', 10), 
            bg="#ffffff", 
            fg="#666666"
        ).pack(pady=(0, 30))
        

        btn_calendario = tk.Button(
            frame_pos_login, 
            text="📅 Abrir Calendário", 
            command=self.abrir_janela2, 
            font=('Helvetica', 12), 
            fg=self.cor_texto, 
            bg=self.cor_destaque,
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=10,
            activebackground="#e04a1a",
            activeforeground="#ffffff"
        )
        btn_calendario.pack(pady=20, ipadx=10, ipady=5)
        

        frame_info = tk.Frame(frame_pos_login, bg="#f8f9fa", bd=1, relief=tk.SUNKEN)
        frame_info.pack(fill=tk.X, pady=20)
        
        tk.Label(
            frame_info, 
            text="Sistema Premium v1.0\nÚltimo acesso: agora", 
            font=('Helvetica', 8), 
            bg="#f8f9fa", 
            fg="#666666",
            justify=tk.LEFT
        ).pack(padx=10, pady=10, anchor=tk.W)
        

        btn_sair = tk.Button(
            frame_pos_login, 
            text="Sair do Sistema", 
            command=self.janela_pos_login.destroy,
            font=('Helvetica', 9), 
            fg="#ffffff", 
            bg="#6c757d",
            relief=tk.FLAT,
            bd=0,
            padx=15,
            pady=5
        )
        btn_sair.pack(side=tk.BOTTOM, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaLogin(root)
    root.mainloop()