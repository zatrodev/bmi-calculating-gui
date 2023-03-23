import tkinter as tk
from tkinter import ttk

from interface.screen_manager import screen_manager


class HomeScreen(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.command_text = tk.StringVar()

        command = tk.Entry(self, textvariable=self.command_text)
        command.grid(row=0, column=1, padx=5, pady=5)

        style = ttk.Style()
        style.configure('W.TButton', font=('calibri', 14, 'bold'))

        enter_button = ttk.Button(
            self, text="Enter Command", style="W.TButton", command=self.process_command)
        enter_button.grid(row=1, column=1, padx=15, pady=10)

        first_label = tk.Label(self, text="1: Record BMI")
        first_label.grid(row=3, column=1, padx=5, pady=5)

        second_label = tk.Label(self, text="2: BMI Display")
        second_label.grid(row=4, column=1, padx=5, pady=5)

    def process_command(self):
        command = self.command_text.get()

        if command == "1":
            screen_manager.switch_screen("")
        elif command == "2":
            screen_manager.switch_screen("user_info")
        else:
            print("Invalid command.")

        self.command_text.set("")
