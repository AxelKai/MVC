
from config.database import get_db_connection

class AttendanceModel:
    def __init__(self):
        self.conn = get_db_connection()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_attendance(self, student_name, status):
        query = "INSERT INTO attendance (student_name, status) VALUES (?, ?)"
        self.conn.execute(query, (student_name, status))
        self.conn.commit()

    def get_all_attendance(self):
        query = "SELECT * FROM attendance"
        cursor = self.conn.execute(query)
        return cursor.fetchall()
