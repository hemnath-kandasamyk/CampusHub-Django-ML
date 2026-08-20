from campushub.student import Student
from campushub.department import Department
from campushub.subject import Subject
from campushub.marks import Mark
from campushub.attendance import Attendance
from campushub.prediction import Prediction


# --------------------------------
# 1. Create Department
# --------------------------------

department = Department(
    1,
    "Artificial Intelligence and Data Science",
    "AI&DS"
)


# --------------------------------
# 2. Create Student
# --------------------------------

student = Student(
    101,
    "Hemnath",
    "hemnath@example.com",
    "AI&DS",
    3
)


# --------------------------------
# 3. Add Student to Department
# --------------------------------

department.add_student(student)


# --------------------------------
# 4. Create Subject
# --------------------------------

subject = Subject(
    101,
    "Machine Learning",
    "ML301",
    4
)


# --------------------------------
# 5. Create Mark
# --------------------------------

mark = Mark(
    student,
    subject,
    45,
    40
)


# --------------------------------
# 6. Create Attendance
# --------------------------------

attendance = Attendance(
    student,
    subject,
    50,
    43
)


# --------------------------------
# 7. Display
# --------------------------------

student.display_profile()

department.display_department()

subject.display_subject()

mark.display_marks()

attendance.display_attendance()