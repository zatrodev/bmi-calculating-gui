import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import os
from dotenv import load_dotenv


class DatabaseService:
    def __new__(cls):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)

        return cls.instance

    def setup_database(self):
        CRED = "./db/bmi-key.json"
        DATABASE_URL = "https://bmi-calculating-machine-default-rtdb.asia-southeast1.firebasedatabase.app/"

        cred = credentials.Certificate(CRED)

        firebase_admin.initialize_app(cred, {
            'databaseURL': DATABASE_URL
        })

        self.db = db

    def get_data_from_reference(self, ref):
        _ref = self.db.reference(ref)

        try:
            return _ref.get()
        except Exception as e:
            raise e

    def set_data_in_reference(self, ref, obj):
        _ref = self.db.reference(ref)

        obj_json = obj.__dict__

        if obj_json is not None:
            try:
                _ref.set(obj_json)
            except Exception as e:
                raise e

    # for development only
    def delete_all(self):
        _ref = self.db.reference("/")
        _ref.delete()


# user_info = UserInfo("Mikko", 18, 425667150008, 40, 1.65)
# service = DatabaseService()
# service.setup_database()
# service.set_data_in_reference(f"/{user_info.lrn}", user_info)
