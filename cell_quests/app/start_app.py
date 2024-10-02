import os
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from app.use_cases import Authenticate, Register, GetQuestions, GetAlternatives, SaveScore, GetScoreboard
from functools import partial
import pygame

class CellQuestApp:
    def __init__(self):
        self.hits = 0
        self.lives = 3
        self.questions = []
        self.current_question_index = 0
        self.option_buttons = []
        self.question_label = None
        self.score_label = None
        self.lives_label = None
        self.username = ""
        self.correct_answer_sound = None
        self.button_click_sound = None
        self.root = tk.Tk()

        pygame.init()
        pygame.mixer.init()

        self.setup_sounds()
        self.setup_ui()
        self.reset_game()

    def setup_sounds(self):
        pygame.mixer.music.load('Perfect Cell Theme Phonk.mp3')
        pygame.mixer.music.play(-1)

        self.button_click_sound = pygame.mixer.Sound('Minecraft Menu Button Sound Effect _ Sounffex.mp3')
        self.correct_answer_sound = pygame.mixer.Sound('Minecraft Menu Button Sound Effect _ Sounffex.mp3')

    def setup_ui(self):
        self.root.title("Cell Quest")
        self.root.geometry("1920x1080")
        self.root.configure(bg="lightblue")

        container = tk.Frame(self.root, bg="lightblue")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        for i in range(3):
            container.grid_rowconfigure(i, weight=1)
            container.grid_columnconfigure(i, weight=1)

        self.create_register_frame(container)
        self.create_login_frame(container)
        self.create_game_frame(container)
        self.create_scoreboard_frame(container)

        self.login_frame.tkraise()

    def create_register_frame(self, container):
        self.register_frame = tk.Frame(container, bg="white", bd=2, relief=tk.RIDGE)
        self.register_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        register_bg_image = Image.open("backgroundlogin.png")
        register_bg_image = register_bg_image.resize((1920, 1080), Image.LANCZOS)
        register_bg_photo = ImageTk.PhotoImage(register_bg_image)

        register_bg_label = tk.Label(self.register_frame, image=register_bg_photo)
        register_bg_label.image = register_bg_photo
        register_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        register_label_frame = tk.Frame(self.register_frame, bg="white")
        register_label_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(register_label_frame, text="Nome de usuário", bg="white", font=("Arial", 18)).grid(row=0, column=0, pady=10, padx=10, sticky="ew")
        self.reg_username_entry = tk.Entry(register_label_frame, font=("Arial", 18), width=20, bd=2, relief=tk.SUNKEN)
        self.reg_username_entry.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        tk.Label(register_label_frame, text="Senha", bg="white", font=("Arial", 18)).grid(row=2, column=0, pady=10, padx=10, sticky="ew")
        self.reg_password_entry = tk.Entry(register_label_frame, show="*", font=("Arial", 18), width=20, bd=2, relief=tk.SUNKEN)
        self.reg_password_entry.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

        tk.Button(register_label_frame, text="Registrar", command=self.register_callback, bg="green", fg="white", font=("Arial", 18), width=15, bd=2, relief=tk.RAISED).grid(row=4, column=0, pady=10, padx=10)
        tk.Button(register_label_frame, text="Voltar ao login", command=self.show_login_window, bg="blue", fg="white", font=("Arial", 18), width=15, bd=2, relief=tk.RAISED).grid(row=5, column=0, pady=10, padx=10)

    def create_login_frame(self, container):
        self.login_frame = tk.Frame(container, bg="white", bd=2, relief=tk.RIDGE)
        self.login_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        login_bg_image = Image.open("backgroundlogin.png")
        login_bg_image = login_bg_image.resize((1920, 1080), Image.LANCZOS)
        login_bg_photo = ImageTk.PhotoImage(login_bg_image)

        login_bg_label = tk.Label(self.login_frame, image=login_bg_photo)
        login_bg_label.image = login_bg_photo
        login_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        login_label_frame = tk.Frame(self.login_frame, bg="white")
        login_label_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(login_label_frame, text="Nome de usuário", bg="white", font=("Arial", 18)).grid(row=0, column=0, pady=10, padx=10, sticky="ew")
        self.username_entry = tk.Entry(login_label_frame, font=("Arial", 18), width=20, bd=2, relief=tk.SUNKEN)
        self.username_entry.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        tk.Label(login_label_frame, text="Senha", bg="white", font=("Arial", 18)).grid(row=2, column=0, pady=10, padx=10, sticky="ew")
        self.password_entry = tk.Entry(login_label_frame, show="*", font=("Arial", 18), width=20, bd=2, relief=tk.SUNKEN)
        self.password_entry.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

        tk.Button(login_label_frame, text="Entrar", command=self.authenticate_callback, bg="blue", fg="white", font=("Arial", 18), width=15, bd=2, relief=tk.RAISED).grid(row=4, column=0, pady=10, padx=10)
        tk.Button(login_label_frame, text="Registrar", command=self.show_register_window, bg="green", fg="white", font=("Arial", 18), width=15, bd=2, relief=tk.RAISED).grid(row=5, column=0, pady=10, padx=10)

    def create_game_frame(self, container):
        self.game_frame = tk.Frame(container, bg="white", bd=2, relief=tk.RIDGE)
        self.game_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        bg_image = Image.open("backgroundlogin.png")
        bg_image = bg_image.resize((1920, 1080), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.game_frame, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.question_label = tk.Label(self.game_frame, text="", wraplength=1800, justify="left", bg="white", font=("Arial", 20))
        self.question_label.grid(row=0, column=0, pady=20, padx=20, sticky="ew")

        self.option_buttons = [tk.Button(self.game_frame, bg="white", font=("Arial", 18), bd=2, relief=tk.RAISED) for _ in range(4)]
        for i, button in enumerate(self.option_buttons):
            button.grid(row=i+1, column=0, sticky="ew", padx=20, pady=10)

        navigation_frame = tk.Frame(self.game_frame, bg="white")
        navigation_frame.grid(row=5, column=0, pady=10)

        tk.Button(navigation_frame, text="Questão Anterior", command=self.previous_question, bg="orange", fg="white", font=("Arial", 18), width=15, bd=2, relief=tk.RAISED).grid(row=0, column=0, pady=10, padx=10)
        tk.Button(navigation_frame, text="Próxima Questão", command=self.next_question, bg="blue", fg="white", font=("Arial", 18), width=15, bd=2, relief=tk.RAISED).grid(row=0, column=1, pady=10, padx=10)

        self.score_label = tk.Label(self.game_frame, text=f"Pontos: {self.hits}", bg="white", font=("Arial", 18))
        self.score_label.grid(row=6, column=0, pady=10, padx=10)

        self.lives_label = tk.Label(self.game_frame, text=f"Vidas: {self.lives}", bg="white", font=("Arial", 18))
        self.lives_label.grid(row=7, column=0, pady=10, padx=10)

        tk.Button(self.game_frame, text="Ver Ranking", command=self.show_scoreboard_frame, bg="purple", fg="white", font=("Arial", 18), width=15, bd=2, relief=tk.RAISED).grid(row=8, column=0, pady=10, padx=10)

        volume_frame = tk.Frame(self.game_frame, bg="white")
        volume_frame.grid(row=9, column=0, pady=10)

        tk.Button(volume_frame, text="Aumentar Volume", command=self.increase_volume, bg="green", fg="white", font=("Arial", 18), width=20, bd=2, relief=tk.RAISED).grid(row=0, column=0, pady=10, padx=10)
        tk.Button(volume_frame, text="Diminuir Volume", command=self.decrease_volume, bg="red", fg="white", font=("Arial", 18), width=20, bd=2, relief=tk.RAISED).grid(row=0, column=1, pady=10, padx=10)

    def create_scoreboard_frame(self, container):
        self.scoreboard_frame = tk.Frame(container, bg="white", bd=2, relief=tk.RIDGE)
        self.scoreboard_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.scoreboard_label = tk.Label(self.scoreboard_frame, text="", bg="white", font=("Arial", 18))
        self.scoreboard_label.pack(pady=20, padx=20)

        tk.Button(self.scoreboard_frame, text="Voltar ao início", command=self.show_login_window, bg="blue", fg="white", font=("Arial", 18), width=15, bd=2, relief=tk.RAISED).pack(pady=10, padx=10)

    def reset_game(self):
        self.hits = 0
        self.lives = 3
        self.current_question_index = 0
        questions_class = GetQuestions()
        self.questions = questions_class.get_questions()
        self.questions.sort(key=lambda q: q[0])
        self.update_lives()
        self.update_score()
        self.load_question(self.current_question_index)

    def update_lives(self):
        self.lives_label.config(text=f"Vidas: {self.lives}")

    def update_score(self):
        self.score_label.config(text=f"Pontos: {self.hits}")

    def load_question(self, index):
        for button in self.option_buttons:
            button.config(bg="white")

        if 0 <= index < len(self.questions):
            self.current_question_index = index
            selected_question = self.questions[self.current_question_index]

            question_id, texto, _, resposta = selected_question
            alternatives_class = GetAlternatives()
            alternatives = alternatives_class.get_alternatives(question_id)

            self.question_label.config(text=f"Questão {question_id}\n{texto}")

            for i, alternative in enumerate(['A', 'B', 'C', 'D']):
                if alternative in alternatives:
                    self.option_buttons[i].config(text=f"{alternative.upper()} - {alternatives[alternative]}", command=partial(self.check_answer, alternative, resposta))
                    self.option_buttons[i].grid(row=i+1, column=0, sticky="w", padx=20, pady=10)
                else:
                    self.option_buttons[i].grid_remove()
        else:
            self.question_label.config(text="Fim das perguntas")
            for button in self.option_buttons:
                button.grid_remove()

    def check_answer(self, selected, correct):
        if selected == correct:
            self.hits += 1
            self.correct_answer_sound.play()
            messagebox.showinfo("Resposta", "Correto!")
            for button in self.option_buttons:
                if button.cget("text").startswith(selected.upper()):
                    button.config(bg="green")
        else:
            self.lives -= 1
            messagebox.showinfo("Resposta", "Errado!")
            for button in self.option_buttons:
                if button.cget("text").startswith(selected.upper()):
                    button.config(bg="red")
                if button.cget("text").startswith(correct.upper()):
                    button.config(bg="green")

        self.update_lives()
        self.update_score()

        if self.lives > 0:
            self.root.after(1000, lambda: self.load_question(self.current_question_index + 1))
        else:
            messagebox.showinfo("Fim de jogo", "Você perdeu todas as vidas!")
            save_score_class = SaveScore()
            save_score_class.save_score(self.username, self.hits)
            self.reset_game()

    def next_question(self):
        self.load_question(self.current_question_index + 1)

    def previous_question(self):
        self.load_question(self.current_question_index - 1)

    def authenticate_callback(self):
        auth_class = Authenticate()
        self.username = self.username_entry.get()
        password = self.password_entry.get()
        if auth_class.authenticate(self.username, password):
            self.game_frame.tkraise()
            self.load_question(self.current_question_index)
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha inválidos")

    def register_callback(self):
        register_class = Register()
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        if register_class.register(username, password):
            messagebox.showinfo("Registro", "Registro bem-sucedido!")
            self.show_login_window()
        else:
            messagebox.showerror("Erro de Registro", "Erro ao registrar usuário")

    def show_register_window(self):
        self.register_frame.tkraise()

    def show_login_window(self):
        self.login_frame.tkraise()

    def show_scoreboard_frame(self):
        scoreboard_class = GetScoreboard()
        scores = scoreboard_class.get_scoreboard()
        scoreboard_text = "\n".join([f"{score['username']}: {score['score']} pontos" for score in scores])
        self.scoreboard_label.config(text=scoreboard_text)
        self.scoreboard_frame.tkraise()

    def increase_volume(self):
        current_volume = pygame.mixer.music.get_volume()
        new_volume = min(current_volume + 0.1, 1.0)
        pygame.mixer.music.set_volume(new_volume)

    def decrease_volume(self):
        current_volume = pygame.mixer.music.get_volume()
        new_volume = max(current_volume - 0.1, 0.0)
        pygame.mixer.music.set_volume(new_volume)

    def start(self):
        self.root.mainloop()

def start_app():
    app = CellQuestApp()
    app.start()
