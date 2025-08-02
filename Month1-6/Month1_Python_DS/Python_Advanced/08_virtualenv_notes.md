# 🐍 `08_virtualenv_notes.md`

## 📌 What is a Virtual Environment?

A **virtual environment** is an isolated environment for Python projects. It allows you to manage dependencies specific to a project, avoiding conflicts with other projects or the system Python.

---

## ⚙️ How to Create and Use a Virtual Environment

### ✅ Step 1: Create a Virtual Environment

```bash
python -m venv venv
```

* `venv` is the folder name. You can change it if you want (e.g., `.venv`, `env`, etc.)

---

### ✅ Step 2: Activate the Virtual Environment

#### ▶️ On **Windows**:

```bash
venv\Scripts\activate
```

#### ▶️ On **macOS/Linux**:

```bash
source venv/bin/activate
```

Once activated, your terminal prompt will change to show the virtual environment name.

---

### ✅ Step 3: Install Packages Inside Virtual Environment

```bash
pip install <package-name>
```

Example:

```bash
pip install requests
```

---

### ✅ Step 4: Freeze Requirements

Save your project’s dependencies:

```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file you can share.

---

### ✅ Step 5: Deactivate the Environment

When you're done:

```bash
deactivate
```

---

### ✅ Step 6: Recreate the Environment from `requirements.txt`

On a new machine or clean setup:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🔁 Best Practices

* Always use a virtual environment per project
* Add `venv/` or `.venv/` to `.gitignore`
* Use `requirements.txt` to share dependencies

---

