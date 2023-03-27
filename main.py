import tkinter as tk

from interface.root import root
from interface.screen_manager import screen_manager
from interface.home_screen import HomeScreen
# from interface.user_info_display import UserInfoDisplay

# from db.firebase import DatabaseService

# db = DatabaseService()
# db.setup_database()

home_screen = HomeScreen(root)
# user_info_screen = UserInfoDisplay(root)

screen_manager.add_screen("home", home_screen)
# screen_manager.add_screen("user_info", user_info_screen)

screen_manager.switch_screen("home")

root.mainloop()
