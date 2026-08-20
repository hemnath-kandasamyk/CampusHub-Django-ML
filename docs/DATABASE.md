# CampusHub — Database Design

## 1. Database Strategy

### Development

SQLite will be used during initial development.

### Production

PostgreSQL will be used for production deployment.

---

## 2. Entities

The CampusHub database contains the following core entities:

1. User
2. Student
3. Department
4. Subject
5. Mark
6. Attendance
7. Prediction

---

## 3. User

Stores authentication information.

| Column | Type | Constraints |
|---|---|---|
| id | Integer | Primary Key |
| username | String | Unique |
| email | String | Unique |
| password | String | Required |
| role | String | Required |

Roles:

- Student
- Faculty
- Admin

---

## 4. Department

Stores department information.

| Column | Type | Constraints |
|---|---|---|
| id | Integer | Primary Key |
| name | String | Required |
| code | String | Unique |

---

## 5. Student

Stores student academic information.

| Column | Type | Constraints |
|---|---|---|
| id | Integer | Primary Key |
| user_id | Integer | Foreign Key |
| roll_number | String | Unique |
| name | String | Required |
| department_id | Integer | Foreign Key |
| year | Integer | Required |
| section | String | Required |

Relationship:

```text
User 1 ───── 1 Student

Department 1 ───── N Student