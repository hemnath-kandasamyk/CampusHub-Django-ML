class Student:

    def __init__(self, student_id, name, email, department, year):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.department = department
        self.__year = year

    def get_year(self):
        return self.__year

    def promote(self):

        if self.__year >= 4:
            print("Student has completed the final year.")
            return

        self.__year += 1
        print(f"{self.name} promoted to year {self.__year}")

    def display_profile(self):

        print("\n===== STUDENT PROFILE =====")
        print("ID         :", self.student_id)
        print("Name       :", self.name)
        print("Email      :", self.email)
        print("Department :", self.department)
        print("Year       :", self.__year)