import tkinter as tk
from tkinter import font as tkfont
import calendar
from datetime import datetime

class ModernCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendário RetroTech Pro")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E2E2E")
        
        # Configurações de estilo
        self.cor_fundo = "#2E2E2E"
        self.cor_destaque = "#4CAF50"
        self.cor_texto = "#FFFFFF"
        self.cor_cabecalho = "#3A3A3A"
        self.cor_dias_semana = "#4A4A4A"
        self.cor_dia_normal = "#3A3A3A"
        self.cor_dia_marcado = "#FF7043"
        self.cor_hoje = "#4CAF50"
        
        # Fontes personalizadas
        self.fonte_titulo = tkfont.Font(family="Segoe UI", size=16, weight="bold")
        self.fonte_dias_semana = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        self.fonte_dias = tkfont.Font(family="Segoe UI", size=10)
        
        # Variáveis de controle
        self.marked_dates = set()
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.today = datetime.now().day
        
        # Cabeçalho
        self.header_frame = tk.Frame(root, bg=self.cor_cabecalho)
        self.header_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        
        self.btn_prev = tk.Button(
            self.header_frame,
            text="◀",
            command=self.prev_month,
            font=self.fonte_titulo,
            bg=self.cor_cabecalho,
            fg=self.cor_texto,
            bd=0,
            activebackground=self.cor_destaque
        )
        self.btn_prev.pack(side=tk.LEFT, padx=10)
        
        self.month_label = tk.Label(
            self.header_frame,
            text="",
            font=self.fonte_titulo,
            bg=self.cor_cabecalho,
            fg=self.cor_texto
        )
        self.month_label.pack(side=tk.LEFT, expand=True)
        
        self.btn_next = tk.Button(
            self.header_frame,
            text="▶",
            command=self.next_month,
            font=self.fonte_titulo,
            bg=self.cor_cabecalho,
            fg=self.cor_texto,
            bd=0,
            activebackground=self.cor_destaque
        )
        self.btn_next.pack(side=tk.RIGHT, padx=10)
        
        # Dias da semana
        self.weekdays_frame = tk.Frame(root, bg=self.cor_fundo)
        self.weekdays_frame.pack(fill=tk.X, padx=20)
        
        weekdays = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
        for i, day in enumerate(weekdays):
            tk.Label(
                self.weekdays_frame,
                text=day,
                font=self.fonte_dias_semana,
                bg=self.cor_dias_semana,
                fg=self.cor_texto,
                width=8,
                padx=5,
                pady=5
            ).grid(row=0, column=i, sticky="ew")
        
        # Calendário
        self.calendar_frame = tk.Frame(root, bg=self.cor_fundo)
        self.calendar_frame.pack(padx=20, pady=(0, 20), expand=True, fill=tk.BOTH)
        
        self.draw_calendar()
    
    def draw_calendar(self):
        # Atualiza o cabeçalho
        self.month_label.config(
            text=f"{calendar.month_name[self.current_month]} {self.current_year}"
        )
        
        # Limpa o frame do calendário
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        
        # Obtém os dados do mês
        month_calendar = calendar.monthcalendar(self.current_year, self.current_month)
        
        # Desenha os dias
        for r, week in enumerate(month_calendar):
            for c, day in enumerate(week):
                if day == 0:
                    # Dia vazio (fora do mês atual)
                    tk.Label(
                        self.calendar_frame,
                        text="",
                        bg=self.cor_fundo,
                        width=8,
                        height=2
                    ).grid(row=r, column=c, padx=2, pady=2)
                else:
                    # Verifica se é hoje
                    is_today = (day == self.today and 
                               self.current_month == datetime.now().month and 
                               self.current_year == datetime.now().year)
                    
                    # Verifica se está marcado
                    is_marked = (self.current_year, self.current_month, day) in self.marked_dates
                    
                    # Configurações visuais
                    bg_color = self.cor_hoje if is_today else (
                        self.cor_dia_marcado if is_marked else self.cor_dia_normal
                    )
                    fg_color = "#000000" if is_today else self.cor_texto
                    
                    # Cria o botão do dia
                    day_btn = tk.Button(
                        self.calendar_frame,
                        text=str(day),
                        font=self.fonte_dias,
                        bg=bg_color,
                        fg=fg_color,
                        width=8,
                        height=2,
                        relief=tk.FLAT,
                        bd=0,
                        activebackground=self.cor_destaque,
                        command=lambda d=day: self.toggle_mark_date(d)
                    )
                    day_btn.grid(row=r, column=c, padx=2, pady=2)
    
    def toggle_mark_date(self, day):
        date = (self.current_year, self.current_month, day)
        if date in self.marked_dates:
            self.marked_dates.remove(date)
        else:
            self.marked_dates.add(date)
        self.draw_calendar()
    
    def prev_month(self):
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.draw_calendar()
    
    def next_month(self):
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.draw_calendar()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalendarApp(root)
    root.mainloop()