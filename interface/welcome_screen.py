import tkinter as tk


class WelcomeScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        title_label = tk.Label(self, text="BMI Calculating Machine",
                               font=("Arial Bold", 36), bg="#f0f0f0")

        subtitle_label = tk.Label(
            self, text="Step on the scale to begin.", font=("Arial", 24), bg="#f0f0f0")

        title_label.pack()
        subtitle_label.pack()
