from db.sql_db import DatabaseService

db = DatabaseService()
db.c.execute("DELETE FROM users")
db.conn.commit()
db.close()
