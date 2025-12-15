

# 🗓️ **Day 4 – SQL JOINs (Tables ko jorna)**

## 🧠 ONE-LINE idea

> **JOIN = 2 tables ko common column ke through connect karna**

Real life example 👇

> “Employee ka **name** aur uske **department ka location** batao”

Name ek table me hai
Location doosri table me
→ JOIN use hoga

---

## 1️⃣ Tables samjho (visual first)

### **employees**

| emp_id | name  | dept_id | salary |
| ------ | ----- | ------- | ------ |
| 1      | John  | 1       | 50000  |
| 2      | Mary  | 2       | 60000  |
| 3      | Peter | 3       | 70000  |
| 4      | Jane  | 4       | 80000  |
| 5      | David | 1       | 55000  |

### **departments**

| dept_id | dept_name | location  |
| ------- | --------- | --------- |
| 1       | IT        | Karachi   |
| 2       | HR        | Lahore    |
| 3       | Finance   | Islamabad |
| 4       | Marketing | Karachi   |

👉 **Common column = dept_id**

---

## 2️⃣ Sab se pehle: INNER JOIN (MOST IMPORTANT)

### 👉 Employee + Department info

```sql
SELECT e.name, d.dept_name, d.location
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;
```

🧠 Simple words:

* `employees e` → e shortcut
* `departments d` → d shortcut
* `ON` → join condition

📌 INNER JOIN:

> Sirf **matching records** deta hai

---

## 3️⃣ LEFT JOIN (left table full)

### 👉 Sab employees + dept info (agar ho)

```sql
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id;
```

🧠 Matlab:

* Left table = employees
* Dept missing ho to bhi employee aayega
* Dept data NULL hoga

---

## 4️⃣ RIGHT JOIN ❌ (SQLite me nahi hota)

SQLite **RIGHT JOIN support nahi karta**
👉 Alternative:

```sql
-- RIGHT JOIN ka kaam
SELECT e.name, d.dept_name
FROM departments d
LEFT JOIN employees e
ON e.dept_id = d.dept_id;
```

---

## 5️⃣ JOIN + WHERE

### 👉 Karachi walay departments ke employees

```sql
SELECT e.name, d.dept_name, d.location
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
WHERE d.location = 'Karachi';
```

---

## 6️⃣ JOIN + GROUP BY (🔥 real power)

### 👉 Department-wise employee count

```sql
SELECT d.dept_name, COUNT(e.emp_id) AS total
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
```

---

## 7️⃣ Python + SQLite (FULL Day 4 code)

`04_joins.py` me run karo 👇

```python
import sqlite3
import pandas as pd
import os

os.makedirs('Database', exist_ok=True)
conn = sqlite3.connect('Database/week21.db')
cur = conn.cursor()

# Create departments table
cur.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT,
    location TEXT
)
""")

# Insert departments data
departments_data = [
    (1, 'IT', 'Karachi'),
    (2, 'HR', 'Lahore'),
    (3, 'Finance', 'Islamabad'),
    (4, 'Marketing', 'Karachi')
]

cur.executemany(
    "INSERT OR IGNORE INTO departments VALUES (?, ?, ?)",
    departments_data
)
conn.commit()

# INNER JOIN
q1 = """
SELECT e.name, d.dept_name, d.location
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
"""
print(pd.read_sql_query(q1, conn), "\n")

# LEFT JOIN
q2 = """
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id
"""
print(pd.read_sql_query(q2, conn), "\n")

# JOIN + GROUP BY
q3 = """
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
"""
print(pd.read_sql_query(q3, conn))

conn.close()
```

---

## ❌ Common mistakes (ye yaad rakho)

❌ JOIN without ON
❌ Wrong column match
❌ dept name se join (slow & unsafe)

✅ Always:

> **Primary key ↔ Foreign key**

---

## 🧪 Practice (must do)

1️⃣ Employee name + location show karo
2️⃣ Karachi walay departments ke employees
3️⃣ Dept-wise **average salary** (JOIN + GROUP BY)

---

