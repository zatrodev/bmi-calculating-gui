import tkinter as tk
from tkinter import ttk

from db.user_info import UserInfo
from db.sql_db import DatabaseService

from interface.entry_with_placeholder import EntryWithPlaceholder

from sensors.sensor_manager import SensorManager

PRIMARY_FONT_SIZE = 18
SECONDARY_FONT_SIZE = 12

HEIGHT_FROM_GROUND = 1.95


class RecordBMIDisplay(tk.Frame):
    def init(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.db = DatabaseService()

        self.name_entry = EntryWithPlaceholder(self, "Name")
        self.name_entry.grid(row=0, column=0, padx=5, pady=5)

        self.age_entry = EntryWithPlaceholder(self, "Age")
        self.age_entry.grid(row=1, column=0, padx=5, pady=5)

        self.lrn_entry = EntryWithPlaceholder(self, "LRN")
        self.lrn_entry.grid(row=2, column=0, padx=5, pady=(5, 20))

        enter_button = ttk.Button(
            self, text="Enter", command=self.record_bmi)
        enter_button.grid(row=3, column=0, padx=5, pady=(5, 30))

        self.weight_label = tk.Label(self, text="")
        self.weight_label.grid(row=6, column=0, padx=5, pady=5)

        self.height_label = tk.Label(self, text="")
        self.height_label.grid(row=7, column=0, padx=5, pady=5)

        self.bmi_label = tk.Label(self, text="")
        self.bmi_label.grid(row=8, column=0, padx=5, pady=5)

        self.nutritional_guide_label = tk.Message(
            self, text="", width=750, justify="center")
        self.nutritional_guide_label.grid(row=9, column=0, padx=5, pady=5)

        self.label_error = ttk.Label(self, foreground='red')
        self.label_error.grid(row=10, column=0, sticky=tk.S, padx=5)

    def record_bmi(self):
        self.label_error["text"] = ""

        name = self.name_entry.get()
        age = self.age_entry.get()
        lrn = self.lrn_entry.get()

        print(name, age, lrn)

        if (name == "Name" or age == "Age" or lrn == "LRN"):
            self.label_error["text"] = "Please fill all entry fields."
            return

        self.height = SensorManager.get_height()
        self.height -= HEIGHT_FROM_GROUND

        self.weight = SensorManager.get_weight()

        user_info = UserInfo(name, age, lrn, self.weight,
                             self.height)

        self.db.insert_user(user_info)

        self.weight_label.config(
            text="Weight (kg): " + str(self.weight), font=("Arial", PRIMARY_FONT_SIZE))

        self.height_label.config(
            text="Height (m): " + str(self.height), font=("Arial", PRIMARY_FONT_SIZE))

        self.bmi_label.config(
            text="BMI: {:.2f} ({})".format(user_info.bmi, user_info.classification), font=("Arial", PRIMARY_FONT_SIZE))

        self.nutritional_guide_label.config(
            text=user_info.nutritional_guide, font=("Arial Bold", SECONDARY_FONT_SIZE), width=750, justify="center")
