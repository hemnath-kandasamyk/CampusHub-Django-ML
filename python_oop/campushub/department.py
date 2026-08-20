class Department:

    def __init__(self, department_id, name, code):
        self.department_id = department_id
        self.name = name
        self.code = code
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_department(self):
        print("\n===== DEPARTMENT =====")
        print("ID      :", self.department_id)
        print("Name    :", self.name)
        print("Code    :", self.code)
        print("Students:", len(self.students))


# Demo

department = Department(
    1,
    "Artificial Intelligence and Data Science",
    "AI&DS"
)

department.display_department()