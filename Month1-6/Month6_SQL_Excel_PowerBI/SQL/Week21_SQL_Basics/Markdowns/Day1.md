## **Day 1 – SELECT Statements**

### **1️⃣ Goal**

* Basic SELECT queries samajhna
* Specific columns retrieve karna
* All rows ya specific rows dekhna

---

### **2️⃣ Sample Dataset**

Ek simple **`employees`** table bana lete hain:

| emp_id | name  | dept    | salary |
| ------ | ----- | ------- | ------ |
| 1      | Ali   | IT      | 60000  |
| 2      | Sara  | HR      | 50000  |
| 3      | Ahmed | IT      | 70000  |
| 4      | Aisha | Finance | 65000  |
| 5      | Bilal | HR      | 55000  |

---

### **3️⃣ SQL Queries**

#### **a) Select all columns**

```sql
SELECT * FROM employees;
```

**Explanation:**

* `*` ka matlab hai **sab columns select karo**
* Ye poori table return karega

#### **b) Select specific columns**

```sql
SELECT name, salary FROM employees;
```

**Explanation:**

* Sirf `name` aur `salary` columns show honge
* Useful jab poora table nahi chahiye

#### **c) Select distinct values**

```sql
SELECT DISTINCT dept FROM employees;
```

**Explanation:**

* Duplicate values ignore kar deta hai
* Yahan unique departments ka list milega

#### **d) Select with expressions**

```sql
SELECT name, salary, salary * 0.1 AS bonus FROM employees;
```

**Explanation:**

* `salary * 0.1` calculate karke `bonus` column me show karega
* `AS bonus` column ko naam de raha hai

#### **e) Limiting results (optional)**

```sql
SELECT * FROM employees LIMIT 3;
```

**Explanation:**

* Sirf pehle 3 rows show honge
* Useful large tables me

---

### **4️⃣ Practice Exercises**

1. Sirf `name` aur `dept` show karo
2. Employees with salary above 60000 select karo (next day WHERE me cover hoga, par ab simple filter try karo)
3. Total number of employees ka count karo using `SELECT COUNT(*)`

---

### **5️⃣ Tip**

* Hamesha start me `SELECT *` try karo table samajhne ke liye
* Fir specific columns select kar ke queries optimize karo
* Small dataset se practice karo, phir large datasets pe apply karo

---
