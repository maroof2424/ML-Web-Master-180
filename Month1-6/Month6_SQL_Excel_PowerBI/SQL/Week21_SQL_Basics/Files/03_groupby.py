import pandas as pd
import sqlite3
import os

os.makedirs('Database', exist_ok=True)

conn = sqlite3.connect(r'Database\week21.db')
# Dept-wise count

q1 = """SELECT dept, COUNT(*) FROM employees GROUP BY dept;"""
print(pd.read_sql_query(q1, conn))

# Dept-wise average salary

q2 = """SELECT dept, AVG(salary) FROM employees GROUP BY dept;"""
print(pd.read_sql_query(q2, conn))

# Dept-wise max salary

q3 = """SELECT dept, MAX(salary) FROM employees GROUP BY dept;"""
print(pd.read_sql_query(q3, conn))

conn.close()