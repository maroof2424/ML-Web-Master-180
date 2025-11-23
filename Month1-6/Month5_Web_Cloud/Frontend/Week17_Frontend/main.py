import os

base_dir = "Month5_Fullstack/Week17_Frontend"

folders = {
    "01_day1_intro_html_css": ["index.html", "style.css", "README.md"],
    "02_day2_forms_buttons": ["form.html", "style.css", "README.md"],
    "03_day3_flexbox_grid": ["layout.html", "style.css", "README.md"],
    "04_day4_bootstrap_basics": ["bootstrap_demo.html", "README.md"],
    "05_day5_tailwind_basics": ["tailwind_demo.html", "README.md"],
    "06_day6_responsive_ui": ["responsive.html", "README.md"],
    "07_day7_mini_project": ["diabetes_form.html", "style.css", "README.md"]
}


for folder, files in folders.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)  
    for file in files:
        file_path = os.path.join(folder_path, file)
        open(file_path, 'a').close()  

print("Directory structure created successfully!")
