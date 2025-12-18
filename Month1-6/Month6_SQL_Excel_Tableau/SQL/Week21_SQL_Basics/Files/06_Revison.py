import sqlite3
import pandas as pd

# ===============================
# CONNECT DATABASE
# ===============================
conn = sqlite3.connect("Database/week21.db")

print("\n==============================")
print("DAY 6 – SQL REVISION")
print("==============================\n")

# ===============================
# 1️⃣ SELECT (Revision)
# ===============================
print("1️⃣ SELECT – All Employees")
q1 = "SELECT * FROM employees"
print(pd.read_sql_query(q1, conn), "\n")

# ===============================
# 2️⃣ WHERE (Revision)
# ===============================
print("2️⃣ WHERE – Salary > 60000")
q2 = "SELECT * FROM employees WHERE salary > 60000"
print(pd.read_sql_query(q2, conn), "\n")

# ===============================
# 3️⃣ GROUP BY (Revision)
# ===============================
print("3️⃣ GROUP BY – Dept-wise Avg Salary")
q3 = """
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id
"""
print(pd.read_sql_query(q3, conn), "\n")

# ===============================
# 4️⃣ JOIN (Revision)
# ===============================
print("4️⃣ JOIN – Employee + Department")
q4 = """
SELECT e.name, d.dept_name, d.location
FROM employees e
JOIN departments d
ON e.dept_id = d.id
"""
print(pd.read_sql_query(q4, conn), "\n")

# ===============================
# 5️⃣ JOIN + GROUP BY (Boss Level)
# ===============================
print("5️⃣ JOIN + GROUP BY – Dept-wise Total Salary")
q5 = """
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d ON e.dept_id = d.id
GROUP BY d.dept_name
"""
print(pd.read_sql_query(q5, conn), "\n")

# ===============================
# CLOSE CONNECTION
# ===============================
conn.close()

print("✅ Day 6 Revision Complete")
