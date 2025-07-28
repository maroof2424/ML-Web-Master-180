import os

structure = {
    "Month1-6": {
        "Month1_Python_DS": ["Python_Advanced", "DataScience_Basics", "Streamlit_Apps"],
        "Month2_Math_ML": ["Math_Notes", "Statistics", "Data_Preprocessing"],
        "Month3_ML_DL_APIs": ["ML_Models", "FastAPI_Projects", "TensorFlow"],
        "Month4_NLP_CV_LangChain": ["NLP_Projects", "OpenCV", "LangChain_Bots"],
        "Month5_Web_Cloud": ["Frontend", "Backend", "Deployment"],
        "Month6_SQL_Excel_Tableau": ["SQL", "Excel", "Tableau"]
    }
}

def create_structure(base_path, structure):
    for root, subfolders in structure.items():
        root_path = os.path.join(base_path, root)
        os.makedirs(root_path, exist_ok=True)
        create_readme(root_path, f"# {root}\n\nDocument your progress here.")
        
        for folder, sub_subfolders in subfolders.items():
            folder_path = os.path.join(root_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            create_readme(folder_path, f"# {folder}\n\nAdd notes or code here.")
            
            for subfolder in sub_subfolders:
                sub_path = os.path.join(folder_path, subfolder)
                os.makedirs(sub_path, exist_ok=True)
                create_readme(sub_path, f"# {subfolder}\n\nContent for this topic goes here.")

def create_readme(path, content):
    readme_path = os.path.join(path, "README.md")
    with open(readme_path, "w") as f:
        f.write(content)

# Run the script
create_structure(".", structure)
