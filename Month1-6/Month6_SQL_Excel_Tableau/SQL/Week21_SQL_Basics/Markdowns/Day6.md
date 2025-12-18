

# 🗓️ **Day 6 – SQL Revision Day (Week 21)**

## 🎯 Aaj ka Goal

> **SELECT + WHERE + GROUP BY + JOIN**
> ek flow mein samajh aajaye, bina cheat-sheet dekhe.

Agar aaj ye ho gaya → Week 21 truly DONE ✅

---

## 1️⃣ Big Picture (pehle dimagh set karo)

SQL ka flow hamesha ye hota hai:

```
FROM
→ JOIN
→ WHERE
→ GROUP BY
→ SELECT
→ ORDER BY
→ LIMIT
```

🧠 Yaad rakhne ka tareeqa:

> **Data lao → filter karo → group banao → result dikhao**

---

## 2️⃣ One-table Revision (SELECT + WHERE)

### Q1: Sab employees dikhao

```sql
SELECT * FROM employees;
```

### Q2: Sirf IT department

```sql
SELECT * FROM employees
WHERE dept_id = 1;
```

### Q3: Salary > 60000

```sql
SELECT * FROM employees
WHERE salary > 60000;
```

👉 Agar ye bina soche likh liya → GOOD 👍

---

## 3️⃣ GROUP BY Revision (summary thinking)

### Q4: Department-wise employee count

```sql
SELECT dept_id, COUNT(*) AS total
FROM employees
GROUP BY dept_id;
```

### Q5: Department-wise avg salary

```sql
SELECT dept_id, AVG(salary)
FROM employees
GROUP BY dept_id;
```

🧠 Rule yaad rakho:

> **SELECT me ya GROUP BY column ho, ya aggregate function**

---

## 4️⃣ JOIN Revision (real SQL test)

### Q6: Employee name + department name

```sql
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id;
```

### Q7: Karachi walay employees

```sql
SELECT e.name, d.location
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
WHERE d.location = 'Karachi';
```

👉 Agar JOIN ka `ON` confuse nahi kar raha → progress 🔥

---

## 5️⃣ GROUP BY + JOIN (🔥 boss level)

### Q8: Department-wise total sales

```sql
SELECT d.dept_name, SUM(s.amount) AS total_sales
FROM sales s
JOIN employees e ON s.emp_id = e.emp_id
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
```

Agar ye samajh aa gaya →
🧠 **real-world SQL samajh aa gaya**

---

## 6️⃣ Self-Test (honest check)

Apne aap se poocho:

✅ Kya mujhe pata hai `WHERE` aur `GROUP BY` ka farq?
✅ Kya mujhe pata hai JOIN me kaunsi key match hoti hai?
✅ Kya main business question ko SQL me convert kar sakta hoon?

Agar **2 bhi YES** hain → tum track par ho 👍
Agar NO → Day 6 ka matlab wahi hai: repeat karo.

---

## 7️⃣ Common Mistakes (revision me pakro)

❌ WHERE ko GROUP BY ke baad likhna
❌ JOIN bina ON
❌ dept_name se join karna (slow, wrong)
❌ SELECT me random column daal dena

✅ Best practice:

> **Primary Key ↔ Foreign Key**

---
