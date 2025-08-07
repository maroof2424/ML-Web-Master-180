### ✅ Day 5: Exploratory Data Analysis (EDA) – Part 1

**Goal:** Begin analyzing a real-world dataset (Netflix, FIFA, IMDB, etc.) using Pandas and Matplotlib.

---

#### 📌 Tasks:

1. **Load Dataset**
   - Use `pd.read_csv()` to import your chosen dataset.
   - View basic structure: `.head()`, `.tail()`, `.info()`, `.shape`, `.columns`

2. **Data Overview**
   - Understand column types, missing values, duplicates.
   - Use `.isnull().sum()`, `.duplicated().sum()` and `.describe()`.

3. **Data Cleaning**
   - Drop or fill nulls.
   - Convert datatypes if necessary.
   - Remove duplicates if any.

4. **Exploratory Questions**
   - Form 3–5 basic questions (e.g., "Most common genre?" or "Top rated players?").

---

#### 🧰 Tools:

- `pandas` for data loading & cleaning
- `matplotlib.pyplot` and/or `seaborn` for basic charts
- Dataset Example:  
  - [Netflix Dataset (Kaggle)](https://www.kaggle.com/datasets/shivamb/netflix-shows)  
  - [FIFA 21 Dataset](https://www.kaggle.com/datasets/stefanoleone992/fifa-21-complete-player-dataset)

---

📁 **File to Work On:** `05_mini_project.ipynb`
