import tkinter as tk

from interface.root import root
from interface.screen_manager import screen_manager
from interface.home_screen import HomeScreen
from interface.user_info_display import UserInfoDisplay
from interface.record_bmi_screen import RecordBMIDisplay
from interface.get_bmi_screen import GetBMIDisplay

from db.sql_db import DatabaseService

db = DatabaseService()

home_screen = HomeScreen()
user_info_screen = UserInfoDisplay()
record_bmi_screen = RecordBMIDisplay()
get_bmi_screen = GetBMIDisplay()

screen_manager.add_screen("home", home_screen)
screen_manager.add_screen("user_info", user_info_screen)
screen_manager.add_screen("get_bmi", get_bmi_screen)
screen_manager.add_screen("record_bmi", record_bmi_screen)

screen_manager.switch_screen(name="home")

root.bind("<Escape>", lambda e: screen_manager.switch_screen(
    name="home", event=e))

root.bind("<Return>", lambda e: screen_manager.switch_screen(
    name="record_bmi", event=e))

tk.Label(root, text="Press [ESC] to go back to home").pack(
    side=tk.BOTTOM, pady=(0, 10))

db.close()
root.mainloop()
