import os

base_dir = "Week18_Javascript_API_Fetching"

structure = {
    "Day1_JS_Basics": ["index.html", "script.js", "README.md"],
    "Day2_DOM_DeepDive": ["bmi.html", "style.css", "bmi.js", "README.md"],
    "Day3_Fetch_JSON": ["fetch_test.html", "test.js", "README.md"],
    "Day4_FastAPI_POST": ["index.html", "api.js", "README.md"],
    "Day5_ML_UI_Integration": ["diabetes_form.html", "ml.js", "style.css", "README.md"],
    "Day6_Error_Handling_UX": ["index.html", "ui.js", "style.css", "README.md"],
    "Day7_Mini_Project/project": ["index.html", "style.css", "app.js"],
    "Day7_Mini_Project/project/components": ["loader.html"],
    "Day7_Mini_Project/project/assets/icons": [],
    "backend": ["main.py", "model.pkl", "requirements.txt", "README.md"]
}

for folder, files in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)

    for f in files:
        file_path = os.path.join(folder_path, f)
        with open(file_path, "w") as fp:
            fp.write("")  

print("✔ Week 18 directory structure created successfully!")
