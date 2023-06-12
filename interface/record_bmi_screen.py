import tkinter as tk
from tkinter import ttk

from db.sql_db import DatabaseService

import interface.get_bmi_screen as BMI
from interface.entry_with_placeholder import EntryWithPlaceholder


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

        self.grade_section_entry = EntryWithPlaceholder(
            self, "Grade & Section (Ex.: 12-Faraday)")
        self.grade_section_entry.grid(row=2, column=0, padx=5, pady=(5, 20))
        self.grade_section_entry.bind(
            "<Return>", lambda e: self.record_bmi(event=e))

        self.lrn_entry = EntryWithPlaceholder(self, "LRN")
        self.lrn_entry.grid(row=3, column=0, padx=5, pady=(5, 20))
        self.lrn_entry.bind("<Return>", lambda e: self.record_bmi(event=e))

        enter_button = ttk.Button(
            self, text="Enter", command=self.record_bmi)
        enter_button.grid(row=3, column=0, padx=5, pady=(5, 30))

        self.label_error = ttk.Label(self, foreground='red')
        self.label_error.grid(row=10, column=0, sticky=tk.S, padx=5)

    def record_bmi(self, event=""):
        if BMI.user_info == "" or BMI.user_info == None:
            print("Invalid user info")
            return

        print(BMI.user_info)
        self.label_error["text"] = ""

        name = self.name_entry.get().strip().upper()
        age = self.age_entry.get().strip()
        lrn = self.lrn_entry.get().strip()
        grade_section = self.grade_section_entry.get().strip().upper()

        print(name, age, lrn, grade_section)

        if (name == "Name" or name == "" or age == "Age" or age == "" or lrn == "LRN" or lrn == "" or grade_section == "Grade & Section (Ex.: 12-Faraday)" or grade_section == ""):
            self.label_error["text"] = "Please fill all entry fields."
            return

        BMI.user_info.name = name
        BMI.user_info.age = age
        BMI.user_info.lrn = lrn
        BMI.user_info.grade, BMI.user_info.section = grade_section.split("-")

        self.db.insert_user(BMI.user_info)

        self.label_error = ttk.Label(
            self, text="DATA SAVED", foreground='green')
        self.label_error.grid(row=9, column=0, sticky=tk.S, padx=5)
