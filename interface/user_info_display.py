import tkinter as tk
from tkinter import ttk

from db.sql_db import DatabaseService


class UserInfoDisplay(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.service = DatabaseService()

        self.lrn_entry = tk.Entry(self)
        self.lrn_entry.grid(row=0, column=0, padx=5, pady=5)

        search_button = ttk.Button(
            self, text="Search User", command=self.search_user)
        search_button.grid(row=1, column=0, padx=5, pady=15)

        self.name_label = tk.Label(self, text="")
        self.name_label.grid(row=4, column=0, padx=5, pady=5)

        self.age_label = tk.Label(self, text="")
        self.age_label.grid(row=5, column=0, padx=5, pady=5)

        self.weight_label = tk.Label(self, text="")
        self.weight_label.grid(row=6, column=0, padx=5, pady=5)

        self.height_label = tk.Label(self, text="")
        self.height_label.grid(row=7, column=0, padx=5, pady=5)

        self.bmi_label = tk.Label(self, text="")
        self.bmi_label.grid(row=8, column=0, padx=5, pady=5)

        self.nutritional_guide_label = tk.Label(self, text="")
        self.nutritional_guide_label.grid(row=9, column=0, padx=5, pady=5)

        self.name_label.config(text="", font=("Arial", 24))
        self.age_label.config(text="", font=("Arial", 24))
        self.weight_label.config(text="", font=("Arial", 24))
        self.height_label.config(text="", font=("Arial", 24))
        self.bmi_label.config(text="", font=("Arial", 24))
        self.nutritional_guide_label.config(text="", font=("Arial", 24))

    def search_user(self):
        lrn = self.lrn_entry.get()

        user_info = self.service.get_user_by_lrn(str(lrn))

        if user_info:
            self.name_label.config(text="Name: " +
                                   user_info.name, font=("Arial", 24), fg="#000")

            self.age_label.config(text="Age: " +
                                  str(user_info.age), font=("Arial", 24))

            self.weight_label.config(
                text="Weight (kg): " + str(user_info.weight), font=("Arial", 24))

            self.height_label.config(
                text="Height (m): " + str(user_info.height), font=("Arial", 24))

            self.bmi_label.config(
                text="BMI: {:.2f} ({})".format(user_info.bmi, user_info.classification), font=("Arial", 24))

            self.nutritional_guide_label.config(
                text=user_info.nutritional_guide, font=("Arial Bold", 24))
        else:
            self.empty_labels()
            self.name_label.config(text="Invalid user with lrn \"{}\"".format(
                lrn), font=("Arial", 24), fg="#f00")

    def empty_labels(self):
        self.age_label.config(text="")
        self.weight_label.config(text="")
        self.height_label.config(text="")
        self.bmi_label.config(text="")
        self.nutritional_guide_label.config(text="")
