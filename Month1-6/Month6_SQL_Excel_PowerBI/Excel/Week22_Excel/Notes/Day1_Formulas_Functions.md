
# Day 1 – Excel Formulas & Functions

## Objective
Learn how to automate calculations and apply logical conditions using core Excel formulas.
This forms the foundation for data analysis and dashboards.

---

## 1. SUM Function

### Concept
The `SUM` function adds multiple numeric values or a range of cells.

### Syntax
```

=SUM(number1, number2, ...)
=SUM(range)

```

### Example
If sales values are in cells `B2:B6`:
```

=SUM(B2:B6)

```

### Use Case
- Total sales
- Total revenue
- Monthly or yearly totals

### Best Practice
- Use ranges instead of individual cells.
- Use absolute references (`$B$2:$B$6`) if the formula will be reused.

---

## 2. AVERAGE Function

### Concept
The `AVERAGE` function calculates the mean of numeric values.

### Syntax
```

=AVERAGE(range)

```

### Example
```

=AVERAGE(B2:B6)

```

### Use Case
- Average sales
- Average score
- Performance metrics

### Best Practice
- Ensure the range contains only numeric values.
- Blank cells are ignored, but text cells can affect results.

---

## 3. IF Function (Conditional Logic)

### Concept
The `IF` function allows decision-making in Excel based on conditions.

### Syntax
```

=IF(condition, value_if_true, value_if_false)

```

### Example
Give bonus if sales are greater than 150:
```

=IF(B2 > 150, "Bonus", "No Bonus")

```

### Use Case
- Pass / Fail
- Bonus eligibility
- Risk classification

### Best Practice
- Keep conditions simple.
- Use clear output labels for readability.

---

## 4. Nested IF (Multiple Conditions)

### Concept
Nested IF handles more than one condition.

### Example
```

=IF(B2 > 200, "High",
IF(B2 > 150, "Medium", "Low"))

```

### Use Case
- Performance grading
- Customer segmentation

### Best Practice
- Avoid too many nested IFs (hard to read).
- Later, prefer `IFS()` or lookup-based logic.

---

## 5. VLOOKUP Function

### Concept
`VLOOKUP` searches for a value in the first column of a table and returns a corresponding value from another column.

### Syntax
```

=VLOOKUP(lookup_value, table_array, col_index, [range_lookup])

```

### Example
Lookup product price:
```

=VLOOKUP("B", $A$2:$B$6, 2, FALSE)

```

### Explanation
- `"B"` → value to search
- `$A$2:$B$6` → lookup table
- `2` → column to return
- `FALSE` → exact match

### Use Case
- Price lookup
- Category mapping
- Reference tables

### Best Practice
- Always use `FALSE` for exact matches.
- Lock table ranges using `$`.
- VLOOKUP cannot search to the left (limitation).

---

## 6. Combining IF + VLOOKUP

### Example
Give "High Bonus" if price > 60:
```

=IF(VLOOKUP(A2, $E$2:$F$6, 2, FALSE) > 60,
"High Bonus", "Normal Bonus")

```

### Real-World Use
- Salary slabs
- Discount systems
- Rule-based automation

---

## Key Takeaways
- `SUM` and `AVERAGE` handle aggregation.
- `IF` adds decision-making.
- `VLOOKUP` connects data from reference tables.
- Absolute references prevent formula breakage.
- Clean formulas = reliable dashboards.

---
