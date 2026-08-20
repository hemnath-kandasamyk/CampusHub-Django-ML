class Prediction:

    def __init__(
        self,
        student,
        attendance,
        average_marks,
        previous_gpa,
        study_hours,
        backlogs
    ):
        self.student = student
        self.attendance = attendance
        self.average_marks = average_marks
        self.previous_gpa = previous_gpa
        self.study_hours = study_hours
        self.backlogs = backlogs

        self.prediction = None
        self.confidence = None

    def set_result(self, prediction, confidence):
        self.prediction = prediction
        self.confidence = confidence

    def display_prediction(self):

        print("\n===== PERFORMANCE PREDICTION =====")
        print("Student      :", self.student.name)
        print("Attendance   :", self.attendance)
        print("Average Mark :", self.average_marks)
        print("Previous GPA :", self.previous_gpa)
        print("Study Hours  :", self.study_hours)
        print("Backlogs     :", self.backlogs)
        print("Prediction   :", self.prediction)
        print("Confidence   :", self.confidence)