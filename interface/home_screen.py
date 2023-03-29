import tkinter as tk
from tkinter import ttk

from interface.screen_manager import screen_manager


class HomeScreen(tk.Frame):
    def init(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.command_entry = tk.Entry(self)
        self.command_entry.grid(row=0, column=0, padx=5, pady=5)

        style = ttk.Style()
        style.configure('W.TButton', font=('calibri', 14, 'bold'))

        enter_button = ttk.Button(
            self, text="Enter Command", style="W.TButton", command=self.process_command)
        enter_button.grid(row=1, column=0, padx=15, pady=10)

        first_label = tk.Label(self, text="1: Record BMI")
        first_label.grid(row=3, column=0, padx=5, pady=5)

        second_label = tk.Label(self, text="2: BMI Display")
        second_label.grid(row=4, column=0, padx=5, pady=5)

        self.label_error = ttk.Label(self, foreground='red')
        self.label_error.grid(row=1, column=0, sticky=tk.S, padx=5)

    def process_command(self):
        command = self.command_entry.get()

        if command == "1":
            screen_manager.switch_screen("record_bmi")
        elif command == "2":
            screen_manager.switch_screen("user_info")
        else:
            self.label_error["text"] = "Invalid command."

        self.command_entry.delete(0, tk.END)
