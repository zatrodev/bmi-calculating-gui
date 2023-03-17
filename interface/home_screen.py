import tkinter as tk


class HomeScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        button1 = tk.Button(self, text="Get BMI",
                            command="", width=30, height=3)
        button1.pack(side=tk.LEFT, padx=50, pady=20)

        button2 = tk.Button(self, text="Show User Profile",
                            command="", width=30, height=3)
        button2.pack(side=tk.RIGHT, padx=50, pady=20)
