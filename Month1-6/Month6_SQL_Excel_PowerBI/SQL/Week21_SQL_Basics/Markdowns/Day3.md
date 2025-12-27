

# 🗓️ **Day 3 – GROUP BY (Aggregation)**

## 🧠 Sab se pehle ONE LINE samjho

> **GROUP BY = data ko groups me divide karna + har group ka result nikalna**

Real life example 👇

> “Har department ka **average salary** batao”

---

## 1️⃣ GROUP BY kyun chahiye?

Abhi tak tum:

* rows dekh rahe thay (SELECT, WHERE)

Ab tum:

* **summary** chahte ho

  * kitne employees hain?
  * avg salary?
  * max / min salary?

Ye kaam **GROUP BY + aggregate functions** karta hai.

---

## 2️⃣ Aggregate Functions (yaad rakhna)

| Function  | Kaam       |
| --------- | ---------- |
| `COUNT()` | rows count |
| `SUM()`   | total      |
| `AVG()`   | average    |
| `MAX()`   | maximum    |
| `MIN()`   | minimum    |

---

## 3️⃣ Sab se SIMPLE example

### 👉 Total employees

```sql
SELECT COUNT(*) FROM employees;
```

📌 Output: `5`

---

## 4️⃣ Department-wise employees count

### 👉 Har department me kitne log hain

```sql
SELECT dept, COUNT(*) 
FROM employees
GROUP BY dept;
```

🧠 Breakdown:

* `GROUP BY dept` → dept ke hisaab se groups
* `COUNT(*)` → har group ka count

📊 Result jaisa:

```
IT        → 2
HR        → 1
Finance   → 1
Marketing → 1
```

---

## 5️⃣ Department-wise average salary (MOST IMPORTANT)

```sql
SELECT dept, AVG(salary) 
FROM employees
GROUP BY dept;
```

🧠 Matlab:

> “Har department ki avg salary batao”

---

## 6️⃣ MAX / MIN salary per department

```sql
SELECT dept, MAX(salary) 
FROM employees
GROUP BY dept;
```

```sql
SELECT dept, MIN(salary) 
FROM employees
GROUP BY dept;
```

---

## 7️⃣ WHERE + GROUP BY (combo)

⚠️ Rule yaad rakho:

> **WHERE pehle, GROUP BY baad me**

### 👉 Sirf salary > 55000 walon ka dept-wise average

```sql
SELECT dept, AVG(salary)
FROM employees
WHERE salary > 55000
GROUP BY dept;
```

---

## 8️⃣ Python + SQLite (Day 3 ready code)

`03_groupby.py` ya notebook me run karo 👇

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('Database/week21.db')

# Dept-wise count
q1 = """
SELECT dept, COUNT(*) AS total_employees
FROM employees
GROUP BY dept
"""
print(pd.read_sql_query(q1, conn), "\n")

# Dept-wise average salary
q2 = """
SELECT dept, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept
"""
print(pd.read_sql_query(q2, conn), "\n")

# Dept-wise max salary
q3 = """
SELECT dept, MAX(salary) AS max_salary
FROM employees
GROUP BY dept
"""
print(pd.read_sql_query(q3, conn))

conn.close()
```

---

## ❌ Common mistakes (avoid karo)

❌ Ye ghalat hai:

```sql
SELECT name, AVG(salary)
FROM employees
GROUP BY dept;
```

🛑 Reason:

* `name` group ka part nahi hai
* SQL confuse ho jata hai

✅ Rule:

> **SELECT me ya to GROUP BY wali column ho, ya aggregate function**

---

## 🧪 Practice (must do)

Khud likho 👇

1️⃣ Har department ka **total salary**
2️⃣ Har department ka **minimum salary**
3️⃣ Salary > 60000 walon ka dept-wise count

---