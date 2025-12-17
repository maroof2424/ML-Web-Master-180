
# 🗓️ **Day 5 – Mini SQL Project**

## 📊 **Project: Company Sales Analysis**

### 🎯 Goal

Business ko ye questions ka answer chahiye:

1. Total sales kitni hui?
2. Department-wise sales?
3. City-wise sales?
4. Top performing employee?
5. IT department ki total sales?

---

## 1️⃣ Database Tables (socho pehle)

### 🧑‍💼 employees

| emp_id | name  | dept_id |
| ------ | ----- | ------- |
| 1      | John  | 1       |
| 2      | Mary  | 2       |
| 3      | Peter | 3       |
| 4      | Jane  | 4       |
| 5      | David | 1       |

### 🏢 departments

| dept_id | dept_name | location  |
| ------- | --------- | --------- |
| 1       | IT        | Karachi   |
| 2       | HR        | Lahore    |
| 3       | Finance   | Islamabad |
| 4       | Marketing | Karachi   |

### 💰 sales

| sale_id | emp_id | amount |
| ------- | ------ | ------ |
| 1       | 1      | 20000  |
| 2       | 1      | 15000  |
| 3       | 2      | 30000  |
| 4       | 3      | 40000  |
| 5       | 4      | 50000  |
| 6       | 5      | 25000  |

---

## 2️⃣ Python + SQLite (FULL PROJECT CODE)

👉 `05_mini_project.py` me paste karo

```python
import sqlite3
import pandas as pd
import os

os.makedirs('Database', exist_ok=True)
conn = sqlite3.connect('Database/week21.db')
cur = conn.cursor()

# ---- SALES TABLE ----
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    amount REAL
)
""")

sales_data = [
    (1, 1, 20000),
    (2, 1, 15000),
    (3, 2, 30000),
    (4, 3, 40000),
    (5, 4, 50000),
    (6, 5, 25000)
]

cur.executemany(
    "INSERT OR IGNORE INTO sales VALUES (?, ?, ?)",
    sales_data
)
conn.commit()
```

---

## 3️⃣ Business Questions + SQL Answers

---

### ✅ 1. Total Sales

```sql
SELECT SUM(amount) AS total_sales
FROM sales;
```

🧠 Simple sum of all sales.

---

### ✅ 2. Employee-wise Total Sales

```sql
SELECT e.name, SUM(s.amount) AS total_sales
FROM employees e
JOIN sales s ON e.emp_id = s.emp_id
GROUP BY e.name;
```

🔥 JOIN + GROUP BY combo.

---

### ✅ 3. Department-wise Sales

```sql
SELECT d.dept_name, SUM(s.amount) AS dept_sales
FROM sales s
JOIN employees e ON s.emp_id = e.emp_id
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
```

🧠 Flow:

```
sales → employees → departments
```

---

### ✅ 4. City-wise Sales

```sql
SELECT d.location, SUM(s.amount) AS city_sales
FROM sales s
JOIN employees e ON s.emp_id = e.emp_id
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.location;
```

---

### ✅ 5. Top Performing Employee

```sql
SELECT e.name, SUM(s.amount) AS total_sales
FROM employees e
JOIN sales s ON e.emp_id = s.emp_id
GROUP BY e.name
ORDER BY total_sales DESC
LIMIT 1;
```

🏆 Business ka hero kaun hai? → ye query batayegi.

---

### ✅ 6. IT Department Total Sales

```sql
SELECT SUM(s.amount) AS it_sales
FROM sales s
JOIN employees e ON s.emp_id = e.emp_id
JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';
```

---

## 4️⃣ Pandas se Result Dekhna

```python
queries = {
    "Total Sales": "SELECT SUM(amount) FROM sales",
    "Dept Sales": """
        SELECT d.dept_name, SUM(s.amount)
        FROM sales s
        JOIN employees e ON s.emp_id = e.emp_id
        JOIN departments d ON e.dept_id = d.dept_id
        GROUP BY d.dept_name
    """
}

for title, q in queries.items():
    print(f"\n{title}")
    print(pd.read_sql_query(q, conn))

conn.close()
```

---

## ❌ Common Mistakes (real talk)

* JOIN ka order confuse karna
* GROUP BY me column miss karna
* Business question samjhe baghair query likhna

👉 **Pehlay question likho, phir SQL**

---

