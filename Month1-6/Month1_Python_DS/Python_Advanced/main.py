import os

# Directory and filenames
folder_name = "Python_Advanced"
files = [
    "01_list_comprehension.py",
    "02_lambda_map_filter_reduce.py",
    "03_decorators_generators.py",
    "04_exception_handling.py",
    "05_file_handling.py",
    "06_oop.py",
    "07_modules_packages.py",
    "08_virtualenv_notes.md",
    "09_type_hinting_docstrings.py",
    "README.md"
]

# Create directory
os.makedirs(folder_name, exist_ok=True)

# Create each file in the directory
for file in files:
    file_path = os.path.join(folder_name, file)
    with open(file_path, "w") as f:
        f.write("")  # Creates empty file

print(f"✅ All files created in '{folder_name}' folder.")
