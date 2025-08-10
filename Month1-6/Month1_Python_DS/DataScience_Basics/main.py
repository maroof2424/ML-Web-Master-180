# import os
# import nbformat as nbf

# base_dir = "Week2-Numpy+Pandas"
# files = [
#     "01_numpy_basics.ipynb",
#     "02_pandas_basics.ipynb",
#     "03_pandas_advanced.ipynb",
#     "04_data_cleaning.ipynb",
#     "05_mini_project.ipynb",
#     "README.md"
# ]

# # Create directory
# os.makedirs(base_dir, exist_ok=True)

# # Create Jupyter notebooks with a sample cell
# for file in files:
#     path = os.path.join(base_dir, file)
#     if file.endswith(".ipynb"):
#         nb = nbf.v4.new_notebook()
#         nb['cells'] = [nbf.v4.new_markdown_cell(f"# {file.replace('_', ' ').replace('.ipynb', '').title()}")]
#         with open(path, 'w', encoding='utf-8') as f:
#             nbf.write(nb, f)
#     else:
#         with open(path, 'w', encoding='utf-8') as f:
#             f.write("# 📘 Week 2 – NumPy + Pandas\n\n_This folder contains notebooks and code for Week 2 tasks._")

# print("✅ Proper .ipynb files created.")


import os

# Base directory for Week 3
base_dir = "Week03_Matplotlib_PromptEng"

# List of files to create
files = [
    "01_matplotlib_basics.ipynb",
    "02_heatmaps_advanced.ipynb",
    "03_prompt_engineering_basics.ipynb",
    "04_zero_few_shot_prompts.ipynb",
    "05_mini_task_chatbot.ipynb",
    "README.md"
]

# Create base directory
os.makedirs(base_dir, exist_ok=True)

# Create each file
for file in files:
    file_path = os.path.join(base_dir, file)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("")  # Empty file

print(f"✅ Week 3 directory and files created in: {base_dir}")
