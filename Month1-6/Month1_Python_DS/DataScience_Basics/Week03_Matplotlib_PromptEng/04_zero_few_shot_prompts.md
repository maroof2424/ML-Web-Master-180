
# 📄 `04_prompt_advanced.md`

## **Advanced Prompt Engineering – Day 4**

This session focuses on **Role Prompts, Zero-shot, and Few-shot Prompting** for better AI responses.

---

## **1️⃣ Role Prompts**

* Define a **role** for the AI to play.
* Example:

```text
"You are a Python tutor. Explain recursion to a beginner with an example."
```

* Benefits: AI tailors tone, style, and knowledge to the role.

---

## **2️⃣ Zero-shot Prompting**

* Ask AI to perform a task **without examples**.
* Example:

```text
"Translate the following English sentences to French."
```

* Works well for straightforward, direct tasks.

---

## **3️⃣ Few-shot Prompting**

* Provide **examples** to guide AI before asking the final question.
* Example:

```text
"Translate the following sentences:
English → French
'Hello' → 'Bonjour'
'Goodbye' → 'Au revoir'
'Thank you' → 'Merci'

Now translate: 'See you tomorrow'"
```

* Benefits: AI mimics patterns from examples, better accuracy.

---

## **4️⃣ Multi-turn Prompts**

* Maintain **context** across multiple questions.
* Example:

```text
User: "You are a math tutor. Explain derivatives."
AI: [Explanation]
User: "Now give an example with x^2"
```

* Keeps AI “in role” and consistent.

---

## **5️⃣ Prompt Chaining**

* Use AI outputs as inputs for the next prompt.
* Example:

  1. Generate a summary of a text.
  2. Ask AI to create quiz questions from that summary.

---

## **6️⃣ Mini Practice Tasks**

1. Create a **role prompt** for an AI acting as a **career counselor**.
2. Create a **few-shot prompt** for generating **short poems**.
3. Try a **multi-turn conversation** with AI solving a **math problem step by step**.
4. Implement **prompt chaining**: summarize a paragraph → generate multiple-choice questions.

---

## **7️⃣ Tips**

* Always **iterate**: Refine prompts to improve output.
* Combine **role + few-shot** for maximum control.
* Use **delimiters (` ``` `)** to clearly separate instructions from input data.

---
\