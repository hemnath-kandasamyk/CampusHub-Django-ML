class Student:

    def __init__(self, student_id, name, email, department, year):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.department = department
        self.year = year

    def display_profile(self):
        print("\n===== STUDENT PROFILE =====")
        print("ID         :", self.student_id)
        print("Name       :", self.name)
        print("Email      :", self.email)
        print("Department :", self.department)
        print("Year       :", self.year)


student = Student(
    101,
    "Hemnath",
    "hemnath@example.com",
    "AI & DS",
    3
)

student.display_profile()