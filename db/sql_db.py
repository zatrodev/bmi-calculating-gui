import sqlite3

from db.user_info import UserInfo


class DatabaseService:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                    (name TEXT, age INTEGER, lrn TEXT, weight REAL, height REAL)''')

    def insert_user(self, user):
        self.c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)",
                       (user.name, user.age, user.lrn, user.weight, user.height))
        self.conn.commit()

    def get_user_by_lrn(self, lrn):
        self.c.execute("SELECT * FROM users WHERE lrn=?", (lrn,))

        result = self.c.fetchone()

        if result:
            user = UserInfo(result[0], result[1],
                            result[2], result[3], result[4])
            return user
        else:
            return None

    def close(self):
        self.conn.close()


# service = DatabaseService()
# user1 = service.get_user_by_lrn("12345678")

# if user1:
#     print(user1.weight)
# else:
#     print("Invalid user")

db_service = DatabaseService()
