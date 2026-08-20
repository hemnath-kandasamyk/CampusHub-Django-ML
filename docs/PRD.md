# CampusHub — Product Requirements Document

## 1. Project Overview

CampusHub is a web-based student academic management platform designed to manage student profiles, academic performance, attendance, and machine-learning-based performance predictions.

The system will provide separate functionality for students and administrators/faculty.

---

## 2. Problem Statement

Educational institutions often maintain student information, marks, attendance, and academic performance data across different systems or manually maintained records.

CampusHub aims to provide a centralized platform where academic information can be managed and analyzed in one place.

The system will also use Machine Learning to analyze student-related data and predict academic performance.

---

## 3. Project Objectives

The main objectives are:

1. Create a centralized student management system.
2. Manage student academic information.
3. Manage marks and attendance.
4. Provide student and administrator dashboards.
5. Develop REST APIs for application communication.
6. Build a Machine Learning model for academic performance prediction.
7. Integrate the ML model with the Django backend.
8. Provide useful recommendations based on prediction results.
9. Provide a scalable architecture suitable for future development.

---

## 4. Target Users

### 4.1 Students

Students can:

- Login to the system.
- View their profile.
- View marks.
- View attendance.
- View academic performance.
- View ML-based performance predictions.
- View recommendations.

### 4.2 Faculty / Administrator

Faculty or administrators can:

- Login to the system.
- Create student records.
- Update student records.
- Delete student records.
- Manage subjects.
- Add and update marks.
- Add and update attendance.
- View student performance.
- View ML predictions.

---

## 5. User Roles

The initial system will contain two roles:

### Student

Permissions:

- View own profile.
- View own marks.
- View own attendance.
- View own predictions.

### Administrator / Faculty

Permissions:

- Manage students.
- Manage subjects.
- Manage marks.
- Manage attendance.
- View student performance.
- Access prediction information.

---

## 6. Functional Requirements

### 6.1 Authentication

The system shall provide:

- User login.
- User logout.
- Role-based access.
- Secure password handling.

### 6.2 Student Management

The system shall support:

- Create student.
- View student.
- Update student.
- Delete student.
- Search students.

### 6.3 Subject Management

The system shall support:

- Create subject.
- View subject.
- Update subject.
- Delete subject.

### 6.4 Marks Management

The system shall support:

- Add student marks.
- Update marks.
- View marks.
- Calculate total marks.
- Calculate average marks.

### 6.5 Attendance Management

The system shall support:

- Record attendance.
- Update attendance.
- Calculate attendance percentage.
- View attendance history.

### 6.6 Performance Dashboard

The dashboard shall display:

- Student information.
- Average marks.
- Attendance percentage.
- Academic performance.
- ML prediction.
- Recommendation.

---

## 7. Machine Learning Requirements

The ML system will predict student academic performance.

### Input Features

The initial model may use:

- Attendance percentage.
- Internal marks.
- Assignment score.
- Previous GPA.
- Study hours.
- Number of backlogs.

### Prediction

The model will classify student performance into:

- Good
- Average
- Poor

### ML Pipeline

```text
Dataset
    ↓
Data Cleaning
    ↓
Exploratory Data Analysis
    ↓
Feature Engineering
    ↓
Train/Test Split
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Best Model Selection
    ↓
Model Serialization
    ↓
Django Integration