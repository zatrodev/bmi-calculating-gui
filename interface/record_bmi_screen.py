import tkinter as tk
from tkinter import ttk

from db.user_info import UserInfo
from db.sql_db import DatabaseService

from interface.entry_with_placeholder import EntryWithPlaceholder

from sensors.sensor_manager import SensorManager

PRIMARY_FONT_SIZE = 18
SECONDARY_FONT_SIZE = 12

HEIGHT_FROM_GROUND = 1.92


class RecordBMIDisplay(tk.Frame):
    def init(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.db = DatabaseService()

        self.name_entry = EntryWithPlaceholder(self, "Name")
        self.name_entry.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry.bind("<Return>", lambda e: self.record_bmi(event=e))

        self.age_entry = EntryWithPlaceholder(self, "Age")
        self.age_entry.grid(row=1, column=0, padx=5, pady=5)
        self.age_entry.bind("<Return>", lambda e: self.record_bmi(event=e))

        self.lrn_entry = EntryWithPlaceholder(self, "LRN")
        self.lrn_entry.grid(row=2, column=0, padx=5, pady=(5, 20))
        self.lrn_entry.bind("<Return>", lambda e: self.record_bmi(event=e))

        enter_button = ttk.Button(
            self, text="Enter", command=self.record_bmi)
        enter_button.grid(row=3, column=0, padx=5, pady=(5, 30))

        self.label_error = ttk.Label(self, foreground='red')
        self.label_error.grid(row=10, column=0, sticky=tk.S, padx=5)

    def record_bmi(self, event=""):
        self.label_error["text"] = ""

        name = self.name_entry.get()
        age = self.age_entry.get()
        lrn = self.lrn_entry.get()

        print(name, age, lrn)

        if (name == "Name" or age == "Age" or lrn == "LRN"):
            self.label_error["text"] = "Please fill all entry fields."
            return

        user_info = UserInfo(name, age, lrn, self.weight,
                             self.height)

        self.db.insert_user(user_info)