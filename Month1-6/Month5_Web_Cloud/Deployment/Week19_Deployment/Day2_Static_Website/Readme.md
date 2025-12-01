# 🌎 **Day 2: Deploying Simple Web Apps (Static Websites)**

**Goal:**

1. Static website ka concept samajhna
2. Render + GitHub pages par FREE hosting seekhna
3. Apna HTML/CSS/JS project internet par live karna

---

# ⭐ Step 1 — Static Website kya hota hai?

Static site = sirf **HTML + CSS + JavaScript**
No backend, no database.

Yeh free platforms isko easily host kar dete hain:

### ✔️ **Render** (best free static hosting)

### ✔️ **GitHub Pages** (100% free, no card, no limits)

---

# ⭐ Step 2 — Folder Structure Ready Karo

Apna project is tarah banado:

```
Week19_Deployment/
 └── Day2_Static_Website/
       ├── index.html
       ├── style.css
       └── script.js
```

Bas itna hi chahiye.

---

# ⭐ Step 3 — Deploy on Render (FREE)

### ✔️ Step 3.1 — GitHub Repo Banao

1. GitHub → New Repository
2. Name: `static-website-test`
3. Add your files:

   * index.html
   * style.css
   * script.js

**Commit + Push**

---

# ✔️ Step 3.2 — Render Par Deploy

1. [https://render.com](https://render.com) → Login
2. Click **New** → **Static Site**
3. Choose your GitHub repo
4. Set:

* **Build Command:** *(empty rakho)*
* **Publish Directory:** `/`

5. Click **Deploy**

🎉 **SITE LIVE IN 30 seconds!**

---

# ⭐ Step 4 — Deploy on GitHub Pages (2nd free option)

GitHub Pages bilkul free aur super stable hai.

### Step 4.1 — Repo Settings

1. Go to GitHub repo
2. Settings → Pages
3. Source: `main` branch
4. Folder: `/root`
5. Save

It will give a link like:

```
https://maroof2424.github.io/static-website-test/
```

Bas — live hogaya.

---

# ⭐ Step 5 — Test Your Deployment

HTML kahi bhi open ho raha ho → DONE 🎉

---

# ⭐ Example index.html (for testing)

Yeh test file deploy kar ke check karo:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Deployment Test</title>
    <style>
        body { font-family: Arial; padding: 40px; background: #fafafa; }
        h1 { color: #4CAF50; }
    </style>
</head>
<body>
    <h1>Deployment Successful 🎉</h1>
    <p>Static website is now LIVE!</p>
</body>
</html>
```

---

# ⭐ **Aaj Ka Goal (Day 2)**

✔️ GitHub repo banaya
✔️ Render par static site deploy ki
✔️ GitHub Pages par deploy ki
✔️ First live link generate kiya

Aaj ke baad:

**Tumhara frontend internet par LIVE hoga → backend connect karna bohot easy ho jayega.**

---

