import os

base_dir = ""

# Folder structure with files
structure = {
    "Week05_Math_Notes": [
        "01_vectors.ipynb",
        "02_matrices.ipynb",
        "03_dot_transpose.ipynb",
        "04_determinants.ipynb",
        "05_eigen.ipynb",
        "06_practice.ipynb",
        "README.md",
        "notes.pdf"   # placeholder
    ],
    "Week06_Statistics": [
        "01_central_tendency.ipynb",
        "02_variance_std.ipynb",
        "03_probability.ipynb",
        "04_normal_distribution.ipynb",
        "05_z_pvalues.ipynb",
        "06_hypothesis.ipynb",
        "07_mini_project.ipynb",
        "README.md"
    ],
    "Week07_Data_Preprocessing": [
        "01_nulls.ipynb",
        "02_outliers.ipynb",
        "03_scaling.ipynb",
        "04_encoding.ipynb",
        "05_feature_engineering.ipynb",
        "06_pipeline.ipynb",
        "07_export_pipeline.ipynb",
        "README.md"
    ],
    "Week08_ML_Intro": [
        "01_linear_regression.ipynb",
        "02_logistic_regression.ipynb",
        "03_classification.ipynb",
        "04_overfit_underfit.ipynb",
        "05_train_test.ipynb",
        "06_cross_validation.ipynb",
        "07_titanic_pipeline.ipynb",
        "README.md"
    ]
}

# Function to create directories and files
def create_structure(base, struct):
    for folder, files in struct.items():
        folder_path = os.path.join(base, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                # create empty placeholders
                with open(file_path, "w", encoding="utf-8") as f:
                    if file.endswith(".md"):
                        f.write(f"# {folder} – Notes\n")
                    elif file.endswith(".ipynb"):
                        f.write("{\n \"cells\": [], \"metadata\": {}, \"nbformat\": 4, \"nbformat_minor\": 5 }\n")
                    elif file.endswith(".pdf"):
                        f.write("")  # placeholder for exported notes

if __name__ == "__main__":
    create_structure(base_dir, structure)
    print(f"✅ {base_dir} structure created successfully!")
