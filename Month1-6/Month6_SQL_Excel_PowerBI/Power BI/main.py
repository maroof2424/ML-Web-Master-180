import os

base_dir = "Week23_PowerBI_Dashboards"

days = {
    "Day01_Basics_Data_Loading": ["Day01_Notes.md"],
    "Day02_Data_Cleaning_PowerQuery": ["Day02_Notes.md"],
    "Day03_Data_Modeling": ["Day03_Notes.md"],
    "Day04_KPIs_DAX": ["Day04_Notes.md"],
    "Day05_Filters_Slicers": ["Day05_Notes.md"],
    "Day06_Charts_Storytelling": ["Day06_Notes.md"],
    "Day07_Final_Dashboard_Project": [
        "Day07_Notes.md",
        "Dashboard.pbix"
    ]
}

os.makedirs(base_dir, exist_ok=True)

for day, files in days.items():
    day_path = os.path.join(base_dir, day)
    os.makedirs(day_path, exist_ok=True)

    for file in files:
        file_path = os.path.join(day_path, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {file.replace('_', ' ').replace('.md', '')}\n\n")

data_path = os.path.join(base_dir, "data")
os.makedirs(data_path, exist_ok=True)

with open(os.path.join(data_path, "sales_data.xlsx"), "w") as f:
    pass

with open(os.path.join(base_dir, "README.md"), "w") as f:
    f.write(
        "# Week 23 – Power BI Dashboards\n\n"
        "Topics:\n"
        "- Stories\n"
        "- Filters & Slicers\n"
        "- KPIs\n"
        "- Charts & Dashboards\n"
    )

print("✅ Week 23 Power BI folder structure created successfully!")
