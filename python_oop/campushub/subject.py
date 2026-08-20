class Subject:

    def __init__(self, subject_id, name, code, credits):
        self.subject_id = subject_id
        self.name = name
        self.code = code
        self.credits = credits

    def display_subject(self):
        print("\n===== SUBJECT =====")
        print("ID      :", self.subject_id)
        print("Name    :", self.name)
        print("Code    :", self.code)
        print("Credits :", self.credits)


# Demo

subject = Subject(
    101,
    "Machine Learning",
    "ML301",
    4
)

subject.display_subject()