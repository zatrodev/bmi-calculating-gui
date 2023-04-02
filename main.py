import tkinter as tk
from tkinter import ttk

from interface.root import root
from interface.screen_manager import screen_manager
from interface.home_screen import HomeScreen
from interface.user_info_display import UserInfoDisplay
from interface.record_bmi_screen import RecordBMIDisplay

from db.sql_db import DatabaseService

db = DatabaseService()

home_screen = HomeScreen()
user_info_screen = UserInfoDisplay()
record_bmi_screen = RecordBMIDisplay()

screen_manager.add_screen("home", home_screen)
screen_manager.add_screen("user_info", user_info_screen)
screen_manager.add_screen("record_bmi", record_bmi_screen)

screen_manager.switch_screen(name="home")

root.bind("<Escape>", lambda e: screen_manager.switch_screen(
    name="home", event=e))

ttk.Label(root, text="Press ESC to go back to home").pack(pady=10)

db.close()
root.mainloop()
