import pandas as pd
import sqlite3
import os

os.makedirs('Database', exist_ok=True)

conn = sqlite3.connect(r'Database\week21.db')
curr = conn.cursor()


# Create tables
curr.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER,
    salary REAL
)''')

curr.execute('''
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY,
    dept_name TEXT,
    location TEXT
)''')

# Insert data
employees = [
    (1, 'John Doe', 1, 50000),
    (2, 'Jane Smith', 2, 60000),
    (3, 'Bob Johnson', 1, 55000),
    (4, 'Alice Brown', 3, 70000)
]
curr.executemany('INSERT INTO employees (id, name, dept_id, salary) VALUES (?, ?, ?, ?)', employees)

departments = [
    (1, 'Sales', 'Karachi'),
    (2, 'Marketing', 'Lahore'),
    (3, 'Engineering', 'Islamabad')
]
curr.executemany('INSERT OR IGNORE INTO departments (id, dept_name, location) VALUES (?, ?, ?)', departments)

# INNER JOIN
print("INTER JOIN:")
q1 = """
SELECT e.name, d.dept_name, d.location
FROM employees e
JOIN departments d
ON e.dept_id = d.id
"""
print(pd.read_sql_query(q1, conn), "\n")

# LEFT JOIN
print("LEFT JOIN:")

q2 = """
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.id
"""
print(pd.read_sql_query(q2, conn), "\n")

# JOIN + GROUP BY
print("JOIN + GROUP BY:")
q3 = """
SELECT d.dept_name, COUNT(e.id) AS total_employees
FROM employees e
JOIN departments d
ON e.dept_id = d.id
GROUP BY d.dept_name
"""
print(pd.read_sql_query(q3, conn), "\n")

conn.commit()
conn.close()
