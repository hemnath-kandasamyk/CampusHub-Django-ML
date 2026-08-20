from .user import User


class Student(User):

    def __init__(
        self,
        user_id,
        name,
        email,
        department,
        year
    ):
        # Initialize User
        super().__init__(user_id, name, email)

        self.department = department
        self.__year = year

        # Composition
        self.marks = []
        self.attendance_records = []

    # -----------------------------
    # Add Mark
    # -----------------------------

    def add_mark(self, mark):
        self.marks.append(mark)

    # -----------------------------
    # Add Attendance
    # -----------------------------

    def add_attendance(self, attendance):
        self.attendance_records.append(attendance)

    # -----------------------------
    # Display Academic Records
    # -----------------------------

    def display_academic_records(self):

        print("\n===== ACADEMIC RECORDS =====")

        print("\n--- MARKS ---")

        if not self.marks:
            print("No marks available.")

        for mark in self.marks:
            mark.display_marks()

        print("\n--- ATTENDANCE ---")

        if not self.attendance_records:
            print("No attendance records available.")

        for attendance in self.attendance_records:
            attendance.display_attendance()

    # -----------------------------
    # Display Student Profile
    # -----------------------------

    def display_profile(self):

        print("\n===== STUDENT PROFILE =====")
        print("ID         :", self.user_id)
        print("Name       :", self.name)
        print("Email      :", self.email)
        print("Department :", self.department)
        print("Year       :", self.__year)