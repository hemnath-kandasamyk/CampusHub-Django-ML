from .user import User


class Faculty(User):

    def __init__(self, user_id, name, email, employee_id, department):
        super().__init__(user_id, name, email)

        self.employee_id = employee_id
        self.department = department

    def display_profile(self):

        print("\n===== FACULTY PROFILE =====")
        print("ID         :", self.user_id)
        print("Name       :", self.name)
        print("Email      :", self.email)
        print("Employee ID:", self.employee_id)
        print("Department :", self.department)