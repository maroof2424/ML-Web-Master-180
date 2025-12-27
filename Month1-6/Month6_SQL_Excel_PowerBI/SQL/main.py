import os

base_folder = "Week21_SQL_Basics"

structure = {
    "notebooks": [
        "01_select.py",
        "02_where.py",
        "03_groupby.py",
        "04_joins.py",
        "05_mini_project.py"
    ],
    "README.md": None
}

def create_structure(base, struct):
    for key, value in struct.items():
        path = os.path.join(base, key)
        if isinstance(value, list):
            # Folder
            os.makedirs(path, exist_ok=True)
            for file in value:
                file_path = os.path.join(path, file)
                open(file_path, "w").close()  
        else:
            file_path = path
            open(file_path, "w").close()

os.makedirs(base_folder, exist_ok=True)

# Create the structure
create_structure(base_folder, structure)

print(f"Folder structure created successfully at {base_folder}")
