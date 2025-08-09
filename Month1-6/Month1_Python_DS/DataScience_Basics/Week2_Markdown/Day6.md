## Day 6

---

### **1. Install the required library**

```bash
pip install ydata-profiling pandas
```

---

### **2. Load the FIFA dataset**

If you already have the dataset locally (e.g., `fifa.csv`), load it.
Otherwise, you can use an online dataset like [Kaggle’s FIFA 19](https://www.kaggle.com/karangadiya/fifa19).

```python
import pandas as pd

# Load dataset (update the path to your file)
df = pd.read_csv("fifa.csv")

df.head()
```

---

### **3. Generate Auto EDA with `ydata-profiling`**

```python
from ydata_profiling import ProfileReport

# Create the profiling report
profile = ProfileReport(
    df,
    title="FIFA Dataset EDA Report",
    explorative=True
)

# Save the report to HTML
profile.to_file("fifa_eda_report.html")

print("Report generated: fifa_eda_report.html")
```

---

### **4. View the report**

After running the above code, open **`fifa_eda_report.html`** in your browser.
You’ll get:

* **Dataset overview**: number of variables, missing values, duplicates.
* **Variable details**: distribution plots, missing value patterns, correlations.
* **Interactive visualizations** for categorical & numerical features.
* **Warnings** for high cardinality, constant columns, etc.

---

