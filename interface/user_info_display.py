import tkinter as tk
from tkinter import ttk

from interface.entry_with_placeholder import EntryWithPlaceholder
from db.sql_db import DatabaseService

PRIMARY_FONT_SIZE = 18
SECONDARY_FONT_SIZE = 12


class UserInfoDisplay(tk.Frame):
    def init(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.columnconfigure(tuple(range(10)), weight=1)
        self.rowconfigure(tuple(range(5)), weight=1)

        self.db = DatabaseService()

        self.lrn_entry = EntryWithPlaceholder(self, "LRN")
        self.lrn_entry.grid(row=0, column=0, padx=5, pady=5)

        search_button = ttk.Button(
            self, text="Search User", command=self.search_user)
        search_button.grid(row=1, column=0, padx=5, pady=(5, 30))

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

        self.empty_labels()

    def search_user(self):
        lrn = self.lrn_entry.get()

        user_info = self.db.get_user_by_lrn(str(lrn))

        if user_info:
            self.name_label.config(text="Name: " +
                                   user_info.name, font=("Arial", PRIMARY_FONT_SIZE), fg="#000")

            self.age_label.config(text="Age: " +
                                  str(user_info.age), font=("Arial", PRIMARY_FONT_SIZE))

            self.weight_label.config(
                text="Weight (kg): " + str(user_info.weight), font=("Arial", PRIMARY_FONT_SIZE))

            self.height_label.config(
                text="Height (m): " + str(user_info.height), font=("Arial", PRIMARY_FONT_SIZE))

            self.bmi_label.config(
                text="BMI: {:.2f} ({})".format(user_info.bmi, user_info.classification), font=("Arial", PRIMARY_FONT_SIZE))

            self.nutritional_guide_label.config(
                text=user_info.nutritional_guide, font=("Arial Bold", SECONDARY_FONT_SIZE))
        else:
            self.empty_labels()
            self.name_label.config(text="Invalid user with lrn \"{}\"".format(
                lrn), font=("Arial", PRIMARY_FONT_SIZE), fg="#f00")

    def empty_labels(self):
        self.name_label.config(text="", font=("Arial", PRIMARY_FONT_SIZE))
        self.age_label.config(text="", font=("Arial", PRIMARY_FONT_SIZE))
        self.weight_label.config(text="", font=("Arial", PRIMARY_FONT_SIZE))
        self.height_label.config(text="", font=("Arial", PRIMARY_FONT_SIZE))
        self.bmi_label.config(text="", font=("Arial", PRIMARY_FONT_SIZE))
        self.nutritional_guide_label.config(
            text="", font=("Arial", PRIMARY_FONT_SIZE))
