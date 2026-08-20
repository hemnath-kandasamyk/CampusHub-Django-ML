class User:

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def display_info(self):
        print("\n===== USER =====")
        print("ID    :", self.user_id)
        print("Name  :", self.name)
        print("Email :", self.email)