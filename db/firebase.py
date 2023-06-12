import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from user_info import UserInfo


class DatabaseService:
    def __new__(cls):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)

        return cls.instance

    def setup_database(self):
        CRED = "./db/bmi-key.json"
        DATABASE_URL = "https://bmi-calculating-device-default-rtdb.asia-southeast1.firebasedatabase.app/"

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

        if "lrn" in obj_json:
            obj_json.pop("lrn")

        if "grade" in obj_json:
            obj_json.pop("grade")

        if "section" in obj_json:
            obj_json.pop("section")

        if "sy" in obj_json:
            obj_json.pop("sy")

        if obj_json is not None:
            try:
                _ref.set(obj_json)
            except Exception as e:
                raise e

    # for development only
    def delete_all(self):
        _ref = self.db.reference("/")
        _ref.delete()


if __name__ == "__main__":
    user_info = UserInfo("Brent", 18, 4021020150721,
                         "12", "Faraday", 61, 1.65)
    user_info.calculate_bmi()
    service = DatabaseService()
    service.setup_database()
    service.set_data_in_reference(
        f"/{user_info.sy}/Grade {user_info.grade}/{user_info.section}/{user_info.lrn}", user_info)
