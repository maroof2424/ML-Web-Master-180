# **Day 2 – Lookup & Reference Functions (Concept + Guide)**

## **Objective**

* Learn to retrieve data dynamically from tables.
* Understand **INDEX, MATCH, and XLOOKUP**.
* Move beyond VLOOKUP to **more flexible, reliable lookup methods**.

---

## **1️⃣ Why Not Only VLOOKUP?**

VLOOKUP is good for simple cases, but it has **limitations**:

| Limitation                | Problem Example                                 |
| ------------------------- | ----------------------------------------------- |
| Only left-to-right lookup | Can’t fetch a value in a column left of the key |
| Column index hard-coded   | If columns are inserted, the formula breaks     |
| Slower on large datasets  | Multiple VLOOKUPs slow down Excel               |
| Limited flexibility       | Complex conditions are hard                     |

**Lesson:** Excel professionals often use `INDEX + MATCH` or `XLOOKUP`.

---

## **2️⃣ MATCH Function**

**Purpose:** Find the **position** of a value in a range.

**Syntax:**

```
=MATCH(lookup_value, lookup_array, match_type)
```

* `lookup_value` → value you want to find
* `lookup_array` → the range to search
* `match_type` → 0 for exact, 1 for smallest <= value, -1 for largest >= value

**Example:**
Find row of Product B in column A:

```
=MATCH("B", A2:A6, 0)
```

**Output:** Row number where "B" appears.

---

## **3️⃣ INDEX Function**

**Purpose:** Return a value from a table **based on row and column number**.

**Syntax:**

```
=INDEX(array, row_num, [col_num])
```

**Example:**
Return the value from 3rd row in column B:

```
=INDEX(B2:B6, 3)
```

---

## **4️⃣ INDEX + MATCH**

**Purpose:** Dynamic lookup (left/right, safe from column changes).

**Logic:**

1. MATCH finds the **row number** of the value you want.
2. INDEX fetches the **actual value** from that row.

**Example:**
Get price of Product B (Price in B2:B6, Products in A2:A6):

```
=INDEX(B2:B6, MATCH("B", A2:A6, 0))
```

**Why use this:**

* Works if the lookup column is not the first column.
* Handles dynamic ranges better than VLOOKUP.

---

## **5️⃣ XLOOKUP (Modern Replacement)**

**Purpose:** Simplest and safest lookup in modern Excel.

**Syntax:**

```
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])
```

**Example:**

```
=XLOOKUP("B", A2:A6, B2:B6, "Not Found")
```

**Advantages:**

* Can lookup left or right
* Default exact match
* Cleaner syntax
* Handles missing values (`if_not_found`)

**Industry Tip:** Use XLOOKUP if your Excel version supports it; otherwise, INDEX + MATCH is still standard.

---

## **6️⃣ Real-World Example**

**Scenario:**

* You have Product IDs in Sheet1
* Prices are in Sheet2
* You want to fetch prices dynamically

**Solution (XLOOKUP):**

```
=XLOOKUP(A2, PriceTable[Product], PriceTable[Price])
```

**Fallback (INDEX + MATCH):**

```
=INDEX(PriceTable[Price], MATCH(A2, PriceTable[Product], 0))
```

**Output:** Price of the product automatically updates when Product ID changes.

---

## **7️⃣ Best Practices**

1. Always use **exact match** (`0` in MATCH or default in XLOOKUP).
2. Lock ranges using `$` if you copy formulas.
3. Prefer XLOOKUP for readability, INDEX + MATCH for backward compatibility.
4. Test formulas on **sample datasets** first.

---

## **Key Takeaways**

* `MATCH` = find position
* `INDEX` = fetch value
* `INDEX + MATCH` = dynamic, safe lookup
* `XLOOKUP` = modern, clean, and preferred

