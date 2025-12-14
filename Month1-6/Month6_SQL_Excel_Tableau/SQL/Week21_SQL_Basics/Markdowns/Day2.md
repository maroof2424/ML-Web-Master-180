
# 🗓️ **Day 2 – WHERE Clause (Filtering Data)**

## 🔑 Big Picture (ye yaad rakho)

**SELECT = kya dekhna hai**
**WHERE = kis condition par dekhna hai**

Real life example:

> “Mujhe **sirf IT department** ke employees dikhao”

---

## 1️⃣ WHERE kya karta hai?

`WHERE` **rows ko filter** karta hai.

Table:

```
employees
```

| id | name  | dept      | salary |
| -- | ----- | --------- | ------ |
| 1  | John  | IT        | 50000  |
| 2  | Mary  | HR        | 60000  |
| 3  | Peter | Finance   | 70000  |
| 4  | Jane  | Marketing | 80000  |
| 5  | David | IT        | 55000  |

---

## 2️⃣ Basic WHERE (Equality)

### 👉 Sirf IT employees

```sql
SELECT * FROM employees
WHERE dept = 'IT';
```

📌 Matlab:

* `dept = 'IT'` → jahan department IT ho

---

## 3️⃣ Numbers ke sath WHERE

### 👉 Salary 60000 se zyada

```sql
SELECT * FROM employees
WHERE salary > 60000;
```

### Operators yaad rakho:

```
=   equal
>   greater than
<   less than
>=  greater or equal
<=  less or equal
!=  not equal
```

---

## 4️⃣ Multiple Conditions (AND / OR)

### 👉 IT department **AND** salary > 52000

```sql
SELECT * FROM employees
WHERE dept = 'IT' AND salary > 52000;
```

🧠 AND ka matlab:

> dono condition true honi chahiye

---

### 👉 HR **OR** Finance

```sql
SELECT * FROM employees
WHERE dept = 'HR' OR dept = 'Finance';
```

🧠 OR ka matlab:

> koi ek bhi true ho

---

## 5️⃣ IN (clean & powerful)

### 👉 Multiple values (best practice)

```sql
SELECT * FROM employees
WHERE dept IN ('HR', 'Finance');
```

✅ Ye zyada clean hai
❌ Bar-bar `OR` avoid karo

---

## 6️⃣ BETWEEN (range check)

### 👉 Salary 55000 se 75000 ke beech

```sql
SELECT * FROM employees
WHERE salary BETWEEN 55000 AND 75000;
```

---

## 7️⃣ LIKE (text search)

### 👉 Name J se start hota ho

```sql
SELECT * FROM employees
WHERE name LIKE 'J%';
```

### 👉 Name me "a" ho kahin bhi

```sql
SELECT * FROM employees
WHERE name LIKE '%a%';
```

🧠 `%` = wildcard (anything)

---

## 8️⃣ Python + SQLite (Day 2 complete code)

Isko `02_where.py` ya notebook me run karo 👇

```python
import sqlite3
import pandas as pd
import os

os.makedirs('Database', exist_ok=True)
conn = sqlite3.connect('Database/week21.db')

# Salary > 60000
q1 = "SELECT * FROM employees WHERE salary > 60000"
print(pd.read_sql_query(q1, conn), "\n")

# IT department
q2 = "SELECT * FROM employees WHERE dept = 'IT'"
print(pd.read_sql_query(q2, conn), "\n")

# IT and salary condition
q3 = "SELECT * FROM employees WHERE dept = 'IT' AND salary > 52000"
print(pd.read_sql_query(q3, conn), "\n")

# IN example
q4 = "SELECT * FROM employees WHERE dept IN ('HR', 'Finance')"
print(pd.read_sql_query(q4, conn))

conn.close()
```

---

## 🧪 Practice (bohot important)

Khud ye queries likho:

1️⃣ Salary < 60000
2️⃣ Marketing department
3️⃣ Name me `a` ho
4️⃣ Salary BETWEEN 50000 AND 70000

👉 Jab tak khud type nahi karoge, SQL dimagh me nahi bethega.

---

## ❌ Common mistakes (avoid karo)

* Strings bina quotes ❌ `dept = IT`
* Capital/lowercase confuse hona
* AND / OR ka logic mix karna

---
