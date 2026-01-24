from controllers.attendanceController import AttendanceController
from services.attendanceService import AttendanceService

def main():
    service = AttendanceService()
    controller = AttendanceController(service)

    while True:
        print("\nAttendance Checker")
        print("1. Add Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            status = input("Enter status (Present/Absent): ")
            try:
                controller.submit_attendance(name, status)
                print("Attendance recorded successfully.")
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            records = controller.get_attendance_list()
            for record in records:
                print(f"{record['id']} - {record['student_name']} : {record['status']}")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
