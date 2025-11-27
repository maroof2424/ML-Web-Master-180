

# ⭐ **Day 5 — DOM Manipulation Level-Up**

Aaj tum HTML + JS ko actual control karna seekhoge — yeh real projects ka foundation hoti hai.
Kal hum document ko “touch” karna seekh rahe thay…
Aaj hum **document ko control** karna seekhenge.

---

# 🔥 **Topics for Day 5**

### **1️⃣ Create Elements Dynamically**

Naya HTML element JS se banana:

```js
const div = document.createElement("div");
div.innerText = "Hello Maroof";
document.body.appendChild(div);
```

**Best practice:**
Direct innerHTML use kam karo, XSS ka risk hota hai.

---

### **2️⃣ Remove Elements**

```js
element.remove();
```

Use cases:

* Todo list delete
* Notifications remove
* Dynamic UI clean-up

---

### **3️⃣ Update CSS from JS**

```js
element.style.color = "red";
element.style.background = "black";
```

**Advice:** Bahut zyada inline style avoid — CSS classes best.

---

### **4️⃣ Add / Remove Classes**

Best practice version:

```js
element.classList.add("active");
element.classList.remove("hidden");
```

Modern UI isi technique se banti hai.

---

### **5️⃣ Input + Form Handling**

User ka data lena + validate karna:

```js
const input = document.querySelector("#name");
console.log(input.value);
```

**Real-world tip:** Always sanitize user input.

---

### **6️⃣ Click Events ka Deep Control**

```js
btn.addEventListener("click", () => {
  console.log("Button clicked!");
});
```

---

# 🧠 Mini Practice (Must-do)

Aaj ka chhota project (5–10 min):

**Todo App Lite**

* Input se text lo
* "Add" button par new `<li>` create karo
* Har item ke sath "delete" button ho
* DOM se remove karo

Isse tum pure Day 5 strong ho jaoge.

---

