
# Day 6 — Error Handling + UX Polish

This is Day 6 of the Week 18 roadmap (JavaScript + API Fetching).  
Aaj humne focus kiya **UX improvements**, **error handling**, aur **loading animations** par — jo real-world front-end apps ka backbone hota hai.

---

## 🎯 What You Learn Here

- `try / catch / finally` ka real usage  
- Loader ka smooth show/hide pattern  
- Error messages ko elegant tarike se display karna  
- Empty field validation  
- Internet down, backend down, wrong input — sab ka handling  
- Minimal & clean UI interactions  

Yeh skills tumhe next step mein full ML UI → FastAPI integration mein bohot help karein gi.

---

## 📁 Folder Structure

```

Day06_Error_Handling_UX/
│── index.html      # UI + loader + alert box
│── style.css       # loader animation + alert styles
└── script.js       # try/catch, API call, UX logic

````

---

## 🚀 How to Run

Simply:

1. Folder open karo  
2. `index.html` browser mein run kar do  
3. Input fill karo → "Send" click karo  
4. Loader, alerts, aur error handling ka behavior dekho  

No server required. Pure front-end project.

---

## 🧠 Concepts Covered (Quick Notes)

### ✔ 1. Loader Pattern  
```js
loader.classList.remove("hidden");   // show
loader.classList.add("hidden");      // hide
````

Best practice: UI block mat karo — just show a nice spinning loader.

---

### ✔ 2. Error Handling

```js
try {
   const res = await fetch(url);

   if (!res.ok) throw new Error("Backend error");

} catch (err) {
   showAlert("Something went wrong.", "error");
}
```

Short, clean, predictable.

---

### ✔ 3. Input Validation

```js
if (!value) {
    showAlert("Please enter something!", "error");
    return;
}
```

User ko bina reason confuse mat karo.

---

### ✔ 4. Alert System

```js
showAlert("Success!", "success");
showAlert("Something went wrong", "error");
```

Readable + reusable function.

---

## 🔥 Mini Tasks You Completed

* Fake API request (which fails)
* Error ko gracefully handle karna
* Success + error alerts
* Button disable during request
* Loader animation
* Invalid input check

Real-world apps mein yeh hi polish tumhari quality define karti hai.
