import tkinter as tk

from interface.root import root
from interface.screen_manager import screen_manager
from interface.home_screen import HomeScreen
from interface.user_info_display import UserInfoDisplay
from interface.record_bmi_screen import RecordBMIDisplay

from db.sql_db import db_service

home_screen = HomeScreen(root)
user_info_screen = UserInfoDisplay(root)
record_bmi_screen = RecordBMIDisplay(root)

screen_manager.add_screen("home", home_screen)
screen_manager.add_screen("user_info", user_info_screen)
screen_manager.add_screen("record_bmi", record_bmi_screen)

screen_manager.switch_screen("home")

db_service.close()
root.mainloop()
