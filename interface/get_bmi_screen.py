import tkinter as tk
from tkinter import ttk

from db.user_info import UserInfo

from interface.root import root
from interface.screen_manager import screen_manager

from sensors.sensor_manager import SensorManager

PRIMARY_FONT_SIZE = 18

SECONDARY_FONT_SIZE = 12

HEIGHT_FROM_GROUND = 1.92

user_info = UserInfo()

class GetBMIDisplay(tk.Frame):
    def init(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.weight_label = tk.Label(self, text="")
        self.weight_label.grid(row=0, column=0, padx=5, pady=5)

        self.height_label = tk.Label(self, text="")
        self.height_label.grid(row=1, column=0, padx=5, pady=5)

        self.bmi_label = tk.Label(self, text="")
        self.bmi_label.grid(row=2, column=0, padx=5, pady=5)

        self.nutritional_guide_label = tk.Message(
            self, text="", width=750, justify="center")
        self.nutritional_guide_label.grid(row=3, column=0, padx=5, pady=5)

        self.get_bmi()

    def get_bmi(self):
        self.height = HEIGHT_FROM_GROUND - SensorManager.get_height()
        self.weight = SensorManager.get_weight()

        user_info.weight = self.weight
        user_info.height = self.height
        user_info.calculate_bmi()

        self.weight_label.config(
            text="Weight (kg): " + str(self.weight), font=("Arial", PRIMARY_FONT_SIZE))

        self.height_label.config(
            text="Height (m): " + str(self.height), font=("Arial", PRIMARY_FONT_SIZE))

        self.bmi_label.config(
            text="BMI: {:.2f} ({})".format(user_info.bmi, user_info.classification), font=("Arial", PRIMARY_FONT_SIZE))

        self.nutritional_guide_label.config(
            text=user_info.nutritional_guide, font=("Arial Bold", SECONDARY_FONT_SIZE), width=750, justify="center")
                
        tk.Label(root, text="Press [SPACE] to save BMI").pack(side=tk.BOTTOM, pady=10) 