import tkinter as tk

from interface.welcome_screen import WelcomeScreen
from interface.user_info_display import UserInfoDisplay
from interface.home_screen import HomeScreen


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculating Machine")
        self.geometry("1024x600")
        self.configure(bg="#f0f0f0")

        self.current_screen = None
        self.switch_screen(UserInfoDisplay)

    def switch_screen(self, screen_class):
        if self.current_screen:
            self.current_screen.pack_forget()

        self.current_screen = screen_class(self)
        self.current_screen.pack()
        self.current_screen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
