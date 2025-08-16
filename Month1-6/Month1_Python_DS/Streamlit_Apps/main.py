import os

base_dir = "Week04_Streamlit_AI"

structure = [
    "01_streamlit_basics.py",
    "02_streamlit_with_pandas.py",
    "03_streamlit_visuals.py",
    "04_ai_basics.md",
    "README.md",
    "05_mini_project/app.py",
    "05_mini_project/data.csv",
    "05_mini_project/README.md",
]

for path in structure:
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    if not os.path.exists(full_path): 
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(f"# {os.path.basename(path)} - Week 4 Placeholder\n")

print(f"✅ Week 4 directory structure created successfully in: {base_dir}")
