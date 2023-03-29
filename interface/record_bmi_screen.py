import tkinter as tk
from tkinter import ttk

from db.user_info import UserInfo
from db.sql_db import DatabaseService

from interface.entry_with_placeholder import EntryWithPlaceholder

from sensors.sensor_manager import SensorManager


class RecordBMIDisplay(tk.Frame):
    def init(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.service = DatabaseService()
        getting_bmi_label = tk.Label(self, text="Getting BMI...",
                                     font=("Arial Bold", 36))

        self.height = SensorManager.get_height()
        self.weight = SensorManager.get_weight()

        print(self.height)

        getting_bmi_label.pack_forget()

        self.name_entry = EntryWithPlaceholder(self, "Name")
        self.name_entry.grid(row=0, column=0, padx=5, pady=5)

        self.age_entry = EntryWithPlaceholder(self, "Age")
        self.age_entry.grid(row=1, column=0, padx=5, pady=5)

        self.lrn_entry = EntryWithPlaceholder(self, "LRN")
        self.lrn_entry.grid(row=2, column=0, padx=5, pady=(5, 20))

        enter_button = ttk.Button(
            self, text="Enter", command=self.record_bmi)
        enter_button.grid(row=3, column=0, padx=5, pady=5)

        self.weight_label = tk.Label(self, text="")
        self.weight_label.grid(row=6, column=0, padx=5, pady=5)

        self.height_label = tk.Label(self, text="")
        self.height_label.grid(row=7, column=0, padx=5, pady=5)

        self.bmi_label = tk.Label(self, text="")
        self.bmi_label.grid(row=8, column=0, padx=5, pady=5)

        self.nutritional_guide_label = tk.Label(self, text="")
        self.nutritional_guide_label.grid(row=9, column=0, padx=5, pady=5)

    def record_bmi(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        lrn = self.lrn_entry.get()

        user_info = UserInfo(name, age, lrn, self.weight,
                             self.height)

        self.service.insert_user(user_info)

        self.weight_label.config(
            text="Weight (kg): " + str(self.weight), font=("Arial", 24))

        self.height_label.config(
            text="Height (m): " + str(self.height), font=("Arial", 24))

        self.bmi_label.config(
            text="BMI: {:.2f} ({})".format(user_info.bmi, user_info.classification), font=("Arial", 24))

        self.nutritional_guide_label.config(
            text=user_info.nutritional_guide, font=("Arial Bold", 24))
