from .user import User


class Admin(User):

    def __init__(self, user_id, name, email, admin_level):
        super().__init__(user_id, name, email)

        self.admin_level = admin_level

    def display_profile(self):

        print("\n===== ADMIN PROFILE =====")
        print("ID          :", self.user_id)
        print("Name        :", self.name)
        print("Email       :", self.email)
        print("Admin Level :", self.admin_level)