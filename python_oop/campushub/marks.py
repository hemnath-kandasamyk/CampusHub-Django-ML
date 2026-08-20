class Mark:

    def __init__(self, student, subject, internal_marks, external_marks):
        self.student = student
        self.subject = subject
        self.internal_marks = internal_marks
        self.external_marks = external_marks

    def calculate_total(self):
        return self.internal_marks + self.external_marks

    def display_marks(self):
        total = self.calculate_total()

        print("\n===== MARKS =====")
        print("Student :", self.student.name)
        print("Subject :", self.subject.name)
        print("Internal:", self.internal_marks)
        print("External:", self.external_marks)
        print("Total   :", total)