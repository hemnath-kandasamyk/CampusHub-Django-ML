# CampusHub — System Architecture

## 1. Architecture Overview

CampusHub follows a layered web application architecture.

```text
User
  ↓
Frontend
  ↓
Django REST API
  ↓
Application Services
  ↓
Database / ML Model

```

## 2. High-Level Architecture

                         USER
                           |
                           v
                 +------------------+
                 |    FRONTEND      |
                 |   HTML/CSS/JS    |
                 +--------+---------+
                          |
                     HTTP / JSON
                          |
                          v
                 +------------------+
                 |   DJANGO API     |
                 +--------+---------+
                          |
              +-----------+-----------+
              |                       |
              v                       v
      +---------------+       +---------------+
      |   DATABASE    |       | ML PIPELINE   |
      |               |       |               |
      | Student       |       | Preprocessing |
      | Subject       |       | Model         |
      | Marks         |       | Prediction    |
      | Attendance    |       | Recommendation|
      | Prediction    |       +---------------+
      +---------------+

 ##  3. Frontend Layer

 ``` text 
 The frontend provides the user interface.

Initial technologies:

HTML
CSS
JavaScript

Main screens:

Login
Student Dashboard
Student Profile
Marks
Attendance
Performance Prediction
Admin Dashboard    