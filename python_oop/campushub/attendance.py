class Attendance:

    def __init__(self, student, subject, total_classes, attended_classes):
        self.student = student
        self.subject = subject
        self.total_classes = total_classes
        self.attended_classes = attended_classes

    def calculate_percentage(self):

        if self.total_classes == 0:
            return 0

        return (self.attended_classes / self.total_classes) * 100

    def is_eligible(self):

        return self.calculate_percentage() >= 75

    def display_attendance(self):

        percentage = self.calculate_percentage()

        print("\n===== ATTENDANCE =====")
        print("Student    :", self.student.name)
        print("Subject    :", self.subject.name)
        print("Classes    :", self.total_classes)
        print("Attended   :", self.attended_classes)
        print("Percentage :", round(percentage, 2), "%")
        print("Eligible   :", self.is_eligible())