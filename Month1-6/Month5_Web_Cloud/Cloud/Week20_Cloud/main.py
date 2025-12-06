import os

# Base path
base_path = r"P:\Python\ML-Web-Master-180\Month1-6\Month5_Web_Cloud\Cloud\Week20_Cloud"

# Folder structure
folders = [
    "app",
    "frontend",
    "notebooks"
]

# Files with initial content
files = {
    "README.md": """# 📦 Week 20 – Cloud Basics (Student-Friendly Free Deployment)

### Folder Structure

Month5_Fullstack/Week20_Cloud/
├── app/                       # FastAPI backend + model
├── frontend/                  # Frontend HTML/JS
├── notebooks/                 # For local testing & preprocessing
└── README.md

### Day-by-Day Roadmap

| Day | Focus                    | Task                                                                          |
| --- | ------------------------ | ----------------------------------------------------------------------------- |
| 1   | Cloud Intro              | Understand AWS (S3, Lambda, EC2) + GCP (Colab, Storage, App Engine)           |
| 2   | Static Deployment        | Deploy simple HTML/CSS/JS frontend using Render or HuggingFace Spaces         |
| 3   | FastAPI Backend          | Create main.py, load ML model, define /predict endpoint                       |
| 4   | Pydantic Validation      | Validate JSON input from frontend                                             |
| 5   | TensorFlow/Sklearn Model | Load ANN / sklearn model and integrate with API                               |
| 6   | Full End-to-End ML API   | Frontend → API → Model → Response                                             |
| 7   | Project Wrap-up          | Test, deploy, log, and monitor                                                |
"""
}

# Create directories
for folder in folders:
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)
    print(f"Created folder: {path}")

# Create files
for filename, content in files.items():
    file_path = os.path.join(base_path, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {file_path}")

# Create starter empty files inside app and frontend
starter_files = {
    "app": ["main.py", "model.pkl", "schemas.py", "routes.py", "requirements.txt"],
    "frontend": ["index.html", "script.js"],
    "notebooks": ["train_model.ipynb"]
}

for folder, file_list in starter_files.items():
    for f_name in file_list:
        path = os.path.join(base_path, folder, f_name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {f_name} - starter file")
        print(f"Created starter file: {path}")
