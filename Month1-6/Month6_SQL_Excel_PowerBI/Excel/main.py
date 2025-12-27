import os

# Base folder for Month 6 Week 22
base_folder = "Week22_Excel"

# Excel files to create
excel_files = [
    "01_formulas_functions.xlsx",
    "02_lookup_reference.xlsx",
    "03_conditional_formatting.xlsx",
    "04_charts.xlsx",
    "05_pivot_basics.xlsx",
    "06_pivot_advanced.xlsx",
    "07_mini_project_dashboard.xlsx"
]

# Markdown folder & files
md_folder = os.path.join(base_folder, "Notes")
md_files = [
    "Day1_Formulas_Functions.md",
    "Day2_Lookup_Reference.md",
    "Day3_Conditional_Formatting.md",
    "Day4_Charts.md",
    "Day5_PivotTables_Basics.md",
    "Day6_PivotTables_Advanced.md",
    "Day7_Mini_Project_Dashboard.md"
]

# 1️⃣ Create main folder
os.makedirs(base_folder, exist_ok=True)
print(f"Created folder: {base_folder}")

# 2️⃣ Create Excel files (empty for now)
for file in excel_files:
    file_path = os.path.join(base_folder, file)
    with open(file_path, "w") as f:
        pass  # Just create an empty file
    print(f"Created Excel file: {file_path}")

os.makedirs(md_folder, exist_ok=True)
print(f"Created folder: {md_folder}")

for file in md_files:
    file_path = os.path.join(md_folder, file)
    with open(file_path, "w") as f:
        f.write(f"# {file.replace('.md','')}\n\n")  # Add header
    print(f"Created Markdown file: {file_path}")

print("✅ Week 22 structure created successfully!")
