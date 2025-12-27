import sqlite3
import pandas as pd
import os

# -------------------------------
# Database setup
# -------------------------------
DB_DIR = "Database"
DB_PATH = os.path.join(DB_DIR, "week21.db")

os.makedirs(DB_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# -------------------------------
# Create table
# -------------------------------
cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    dept TEXT,
    salary REAL
)
""")

# -------------------------------
# Insert data (safe check)
# -------------------------------
cur.execute("SELECT COUNT(*) FROM employees")
count = cur.fetchone()[0]

if count == 0:
    employees_data = [
        (1, "John", "IT", 50000),
        (2, "Mary", "HR", 60000),
        (3, "Peter", "Finance", 70000),
        (4, "Jane", "Marketing", 80000),
        (5, "David", "IT", 55000)
    ]

    cur.executemany(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        employees_data
    )
    conn.commit()

# -------------------------------
# DAY 1 – SELECT
# -------------------------------
print("\nDAY 1 - SELECT")
df = pd.read_sql_query(
    "SELECT id, name, salary FROM employees",
    conn
)
print(df)

# -------------------------------
# DAY 2 – WHERE
# -------------------------------
print("\nDAY 2 - WHERE (salary > 55000)")
df = pd.read_sql_query(
    "SELECT * FROM employees WHERE salary > 55000",
    conn
)
print(df)

# -------------------------------
# DAY 3 – GROUP BY
# -------------------------------
print("\nDAY 3 - GROUP BY (avg salary per dept)")
df = pd.read_sql_query(
    """
    SELECT dept, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept
    """,
    conn
)
print(df)

# -------------------------------
# DAY 4 – ORDER BY
# -------------------------------
print("\nDAY 4 - ORDER BY salary DESC")
df = pd.read_sql_query(
    "SELECT * FROM employees ORDER BY salary DESC",
    conn
)
print(df)

# -------------------------------
# DAY 5 – Mini Analysis
# -------------------------------
print("\nDAY 5 - Highest Paid Employee")
df = pd.read_sql_query(
    """
    SELECT name, dept, salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 1
    """,
    conn
)
print(df)

# -------------------------------
# DAY 6 – Revision Summary
# -------------------------------
print("\nDAY 6 - REVISION CHECK")
df = pd.read_sql_query(
    """
    SELECT dept, COUNT(*) AS total_employees, SUM(salary) AS total_salary
    FROM employees
    GROUP BY dept
    """,
    conn
)
print(df)

# -------------------------------
# Close connection
# -------------------------------
conn.close()

print("\nWeek 21 SQL completed successfully.")
