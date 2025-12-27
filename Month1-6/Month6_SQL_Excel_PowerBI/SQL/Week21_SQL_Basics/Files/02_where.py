import pandas as pd
import sqlite3
import os

os.makedirs('Database', exist_ok=True)

conn = sqlite3.connect(r'Database\week21.db')
curr = conn.cursor()

df = pd.read_sql_query("SELECT * FROM employees", conn)
print(df)

# Salary > 60000

q1 = "SELECT * FROM employees WHERE salary > 60000"
curr.execute(q1)

# IT department

q2 = "SELECT * FROM employees WHERE dept = 'IT'"
curr.execute(q2)

# IT and salary condition

q3 = "SELECT * FROM employees WHERE dept = 'IT' AND salary > 60000 "
curr.execute(q3)

# IN example

example = "SELECT * FROM employees WHERE dept IN ('HR','IT')"
print(pd.read_sql_query(example, conn))

conn.commit()
conn.close()
