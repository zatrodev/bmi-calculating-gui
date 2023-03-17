from interface.main import MainApp
from db.firebase import DatabaseService

service = DatabaseService()
service.setup_database()

root = MainApp()
root.mainloop()
