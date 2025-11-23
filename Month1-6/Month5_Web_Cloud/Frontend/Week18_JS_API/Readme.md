# 🗓️ **Week 18 — JavaScript + API Fetching**

**Goal:**
Front-end se FastAPI backend ko call karna, ML model ka result UI par show karna.
Is week ke baad tum 100% ek full working **BMI / Diabetes predictor UI → Backend → Result** pipeline bana loge.

---

# ⭐ **Day 1 → JavaScript Basics Refresher**

**Topics:**

* Variables (let, const)
* Functions
* Arrays & Objects
* DOM basics → `document.querySelector`, `value`, `innerText`

**Mini Task:**
HTML page banao → input lo → button click par console mein print karo.

**Honest Tip:**
JS main `var` avoid karo. Sirf `let` & `const` use karo — cleaner, predictable.

---

# ⭐ **Day 2 → DOM Manipulation Deep Dive**

**Topics:**

* Changing text
* Adding/removing classes
* Creating elements
* Event listeners

**Mini Task:**
BMI calculator front-end only (no backend):

* Weight + height input
* `Calculate` button
* Result show in a card

**Best practice:**
Always attach events using `addEventListener`. Inline `onclick="..."` avoid karo.

---

# ⭐ **Day 3 → JSON + Fetch API Basics**

**Topics:**

* JSON.parse / JSON.stringify
* `fetch()` GET + POST basics
* Promise (`then`, `catch`)
* Error handling

**Mini Task:**
Fake API hit karo:

```
https://jsonplaceholder.typicode.com/posts/1
```

Title ko HTML mein render karo.

**Avoid:**
`fetch().then().then().then()`… chain lamba mat karo → unreadable.

---

# ⭐ **Day 4 → POST Requests to Your FastAPI**

**Topics:**

* Sending JSON body
* `headers: {'Content-Type': 'application/json'}`
* Await + async functions
* Backend se response structure samajhna

**Mini Task:**
Apna pichla FastAPI prediction endpoint use karo.
JS se hit karo → result console mein print karo.

**Friend tip:**
Backend error aata hai? Pehle “CORS” settings check karo. 80% API beginners issi mein phashtay hain.

---

# ⭐ **Day 5 → ML UI Integration**

**Topics:**

* Read values from form
* Validate input
* Show loader
* API call
* Display ML prediction result in a card

**Mini Task:**
Diabetes form (jo humne banaya) → FastAPI ML API ko hit kare → result UI par show kare.

**Example prediction flow (JS):**

* Button click → disable button
* Inputs collect → JSON body send
* Response: `{"prediction": 0}`
* UI updates: “Not diabetic” / “Diabetic”

---

# ⭐ **Day 6 → Error Handling + UX Polish**

**Topics:**

* Try/catch
* Empty fields check
* Loading animation
* API errors gracefully show karna

**Mini Task:**
3 types of errors handle karo:

1. Internet off
2. Backend down
3. Invalid input

UI par red alert box show karo.

**Honest advice:**
Error messages copy/paste mat jamao. Keep them minimal:
“Something went wrong. Try again.”

---

# ⭐ **Day 7 → Mini Project**

**🎯 Full ML UI + API Integration Project**
**You will build:**

* Diabetes form UI
* JS script to collect inputs
* Fetch API POST request
* Show prediction result
* Error handling
* Loading animation

**Output:**
Complete working ML → FastAPI → JS → UI project.

**Optional but recommended:**
Add “Confidence Score %” or “Recommended Tips”.

---