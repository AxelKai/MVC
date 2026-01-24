
from models.attendanceModel import AttendanceModel

class AttendanceService:
    def __init__(self):
        self.model = AttendanceModel()

    def record_attendance(self, student_name, status):
        if not student_name:
            raise ValueError("Student name cannot be empty")

        if status not in ["Present", "Absent"]:
            raise ValueError("Invalid attendance status")

        self.model.add_attendance(student_name, status)

    def fetch_attendance(self):
        return self.model.get_all_attendance()
