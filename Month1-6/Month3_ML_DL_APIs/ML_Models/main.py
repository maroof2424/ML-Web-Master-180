import os

# Base directory
base_dir = "Week09_Sklearn"

# Files for Week 9
files = [
    "01_linear_regression.ipynb",
    "02_logistic_regression.ipynb",
    "03_knn.ipynb",
    "04_decision_tree.ipynb",
    "05_metrics.ipynb",
    "06_model_compare.ipynb",
    "README.md"
]

# Create base directory
os.makedirs(base_dir, exist_ok=True)

# Create empty files
for file in files:
    file_path = os.path.join(base_dir, file)
    with open(file_path, "w", encoding="utf-8") as f:
        if file.endswith(".md"):
            f.write("# 🗓️ Week 9 – ML with Scikit-learn\n")
        else:
            f.write(f"")

print(f"✅ Week 9 directory and files created at: {os.path.abspath(base_dir)}")
