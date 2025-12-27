import pandas as pd
import sqlite3
import os

os.makedirs('Database', exist_ok=True)

conn = sqlite3.connect(r'Database\week21.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            dept TEXT,
            salary REAL
           )""")

employees_data = [
    (1,"John","IT",50000),
    (2,"Mary","HR",60000),
    (3,"Peter","Finance",70000),
    (4,"Jane","Marketing",80000),
    (5,"David","IT",55000)
]

cur.executemany("INSERT INTO employees VALUES(?,?,?,?)", employees_data)

df = pd.read_sql_query("SELECT * FROM employees", conn)
print(df)
df = pd.read_sql_query("SELECT name, salary FROM employees", conn)
print(df)

conn.commit()
conn.close()
