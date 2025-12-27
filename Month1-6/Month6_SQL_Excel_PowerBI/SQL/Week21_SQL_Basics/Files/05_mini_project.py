import sqlite3
import pandas as pd
import os


os.makedirs("Database", exist_ok=True)
conn = sqlite3.connect("Database/week21.db")
cur = conn.cursor()


# Employees
cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER
)
""")

# Departments
cur.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT,
    location TEXT
)
""")

# Sales
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    amount REAL
)
""")


employees_data = [
    (1, "John", 1),
    (2, "Mary", 2),
    (3, "Peter", 3),
    (4, "Jane", 4),
    (5, "David", 1)
]

departments_data = [
    (1, "IT", "Karachi"),
    (2, "HR", "Lahore"),
    (3, "Finance", "Islamabad"),
    (4, "Marketing", "Karachi")
]

sales_data = [
    (1, 1, 20000),
    (2, 1, 15000),
    (3, 2, 30000),
    (4, 3, 40000),
    (5, 4, 50000),
    (6, 5, 25000)
]

cur.executemany(
    "INSERT OR IGNORE INTO employees VALUES (?, ?, ?)",
    employees_data
)

cur.executemany(
    "INSERT OR IGNORE INTO departments VALUES (?, ?, ?)",
    departments_data
)

cur.executemany(
    "INSERT OR IGNORE INTO sales VALUES (?, ?, ?)",
    sales_data
)

conn.commit()


queries = {
    "📌 Total Sales": """
        SELECT SUM(amount) AS total_sales
        FROM sales
    """,

    "📌 Employee-wise Sales": """
        SELECT e.name, SUM(s.amount) AS total_sales
        FROM employees e
        JOIN sales s ON e.emp_id = s.emp_id
        GROUP BY e.name
    """,

    "📌 Department-wise Sales": """
        SELECT d.dept_name, SUM(s.amount) AS dept_sales
        FROM sales s
        JOIN employees e ON s.emp_id = e.emp_id
        JOIN departments d ON e.dept_id = d.dept_id
        GROUP BY d.dept_name
    """,

    "📌 City-wise Sales": """
        SELECT d.location, SUM(s.amount) AS city_sales
        FROM sales s
        JOIN employees e ON s.emp_id = e.emp_id
        JOIN departments d ON e.dept_id = d.dept_id
        GROUP BY d.location
    """,

    "📌 Top Performing Employee": """
        SELECT e.name, SUM(s.amount) AS total_sales
        FROM employees e
        JOIN sales s ON e.emp_id = s.emp_id
        GROUP BY e.name
        ORDER BY total_sales DESC
        LIMIT 1
    """,

    "📌 IT Department Sales": """
        SELECT SUM(s.amount) AS it_sales
        FROM sales s
        JOIN employees e ON s.emp_id = e.emp_id
        JOIN departments d ON e.dept_id = d.dept_id
        WHERE d.dept_name = 'IT'
    """
}


for title, query in queries.items():
    print("\n" + title)
    print(pd.read_sql_query(query, conn))

conn.close()
