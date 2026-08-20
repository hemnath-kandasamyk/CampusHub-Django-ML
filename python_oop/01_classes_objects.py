class Student:

    def __init__(self, name, email, department, year):
        self.name = name
        self.email = email
        self.department = department
        self.year = year

    def display_profile(self):
        print("\n--- Student Profile ---")
        print("Name       :", self.name)
        print("Email      :", self.email)
        print("Department :", self.department)
        print("Year       :", self.year)


student = Student(
    "Hemnath",
    "hemnath@example.com",
    "AI & DS",
    3
)

student.display_profile()