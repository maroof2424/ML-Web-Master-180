## **Day 5 — SpaCy Intro** 

### 🎯 Goal

Learn the basics of **SpaCy** for Natural Language Processing —
👉 Part-of-Speech (POS) Tagging
👉 Named Entity Recognition (NER)
👉 Sentence parsing (Dependency Tree)

---

## 🧩 **Concept Overview**

| Concept                | Description                                                            |
| ---------------------- | ---------------------------------------------------------------------- |
| **POS Tagging**        | Identifies the grammatical role of each word (noun, verb, adj, etc.)   |
| **NER**                | Detects named entities like people, organizations, dates, etc.         |
| **Dependency Parsing** | Understands sentence structure (subject → verb → object relationships) |

---

## ⚙️ **Setup**

If running locally or in Colab:

```bash
!pip install spacy
!python -m spacy download en_core_web_sm
```

---

## 🧠 **Code Walkthrough**

### 1️⃣ Import and Load Model

```python
import spacy

# Load small English model
nlp = spacy.load("en_core_web_sm")
```

---

### 2️⃣ Process a Sentence

```python
text = "Apple is looking at buying a UK-based AI startup for $1 billion."
doc = nlp(text)
```

---

### 3️⃣ POS Tagging (Part of Speech)

```python
for token in doc:
    print(f"{token.text:<15} POS: {token.pos_:<10} | Dep: {token.dep_:<10}")
```

**Output Example:**

```
Apple           POS: PROPN     | Dep: nsubj     
is              POS: AUX       | Dep: aux       
looking         POS: VERB      | Dep: ROOT      
at              POS: ADP       | Dep: prep      
buying          POS: VERB      | Dep: pcomp     
a               POS: DET       | Dep: det       
UK              POS: PROPN     | Dep: compound  
based           POS: ADJ       | Dep: amod      
AI              POS: PROPN     | Dep: compound  
startup         POS: NOUN      | Dep: pobj      
for             POS: ADP       | Dep: prep      
$               POS: SYM       | Dep: quantmod  
1               POS: NUM       | Dep: compound  
billion         POS: NUM       | Dep: pobj      
.               POS: PUNCT     | Dep: punct     
```

---

### 4️⃣ Named Entity Recognition (NER)

```python
for ent in doc.ents:
    print(f"{ent.text:<20} | Label: {ent.label_}")
```

**Example Output:**

```
Apple                | Label: ORG
UK                   | Label: GPE
$1 billion           | Label: MONEY
```

---

### 5️⃣ Visualize Dependencies and Entities

In **Jupyter/Colab**, you can visualize easily:

```python
from spacy import displacy

# Dependency Tree
displacy.render(doc, style="dep", jupyter=True, options={"distance": 90})

# Named Entities
displacy.render(doc, style="ent", jupyter=True)
```

---

### 6️⃣ Sentence Parsing Example

```python
for sent in doc.sents:
    print("Sentence:", sent.text)
```

---

### 🧠 **Mini Task**

Try processing:

```python
text2 = "Elon Musk founded SpaceX in 2002 and Tesla in 2003 in California."
```

👉 Extract:

* Named entities (ORG, PERSON, DATE, GPE)
* POS tags for each word
* Dependency tree visualization

---

### ✅ **Summary**

| Feature                  | Description                       |
| ------------------------ | --------------------------------- |
| `token.pos_`             | Part-of-speech (NOUN, VERB, etc.) |
| `token.dep_`             | Dependency relation               |
| `ent.text`, `ent.label_` | Entity text & type                |
| `displacy.render()`      | Visualize dependencies/entities   |

---