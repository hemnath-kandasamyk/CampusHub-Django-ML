from campushub.student import Student
from campushub.department import Department
from campushub.subject import Subject
from campushub.marks import Mark
from campushub.attendance import Attendance
from campushub.faculty import Faculty
from campushub.admin import Admin


# ==========================================
# 1. CREATE DEPARTMENT
# ==========================================

department = Department(
    1,
    "Artificial Intelligence and Data Science",
    "AI&DS"
)


# ==========================================
# 2. CREATE STUDENT
# ==========================================

student = Student(
    101,
    "Hemnath",
    "hemnath@example.com",
    "AI&DS",
    3
)


# ==========================================
# 3. ADD STUDENT TO DEPARTMENT
# ==========================================

department.add_student(student)


# ==========================================
# 4. CREATE SUBJECT
# ==========================================

subject = Subject(
    101,
    "Machine Learning",
    "ML301",
    4
)


# ==========================================
# 5. CREATE MARK
# ==========================================

mark = Mark(
    student,
    subject,
    45,
    40
)

# Composition
student.add_mark(mark)


# ==========================================
# 6. CREATE ATTENDANCE
# ==========================================

attendance = Attendance(
    student,
    subject,
    50,
    43
)

# Composition
student.add_attendance(attendance)


# ==========================================
# 7. CREATE FACULTY
# ==========================================

faculty = Faculty(
    201,
    "Arun",
    "arun@campushub.com",
    "FAC001",
    "AI&DS"
)


# ==========================================
# 8. CREATE ADMIN
# ==========================================

admin = Admin(
    301,
    "CampusHub Admin",
    "admin@campushub.com",
    "SUPER_ADMIN"
)


# ==========================================
# 9. STUDENT PROFILE
# ==========================================

student.display_profile()


# ==========================================
# 10. DEPARTMENT
# ==========================================

department.display_department()


# ==========================================
# 11. SUBJECT
# ==========================================

subject.display_subject()


# ==========================================
# 12. ACADEMIC RECORDS
# ==========================================

student.display_academic_records()


# ==========================================
# 13. POLYMORPHISM DEMO
# ==========================================

print("\n===== POLYMORPHISM DEMO =====")

users = [
    student,
    faculty,
    admin
]

for user in users:
    user.display_profile()