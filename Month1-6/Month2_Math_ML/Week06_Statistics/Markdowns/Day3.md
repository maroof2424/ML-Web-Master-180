# 📘 Day 3 – Probability

---

## 1. Basics of Probability

Probability measures the **likelihood** of an event occurring.

$$
P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}
$$

Example: Tossing a coin → $P(\text{Head}) = \frac{1}{2}$.

---

## 2. Events & Sample Space

* **Sample Space (S):** All possible outcomes.
  Example: Tossing 1 dice → $S = \{1,2,3,4,5,6\}$.
* **Event (E):** Subset of sample space.
  Example: Getting even number → $E = \{2,4,6\}$.

---

## 3. Independent vs Dependent Events

* **Independent Events:** One event does not affect the other.
  Example: Tossing 2 coins → P(H on 1st ∩ H on 2nd) = $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.

* **Dependent Events:** One event affects the probability of the other.
  Example: Drawing cards without replacement.

---

## 4. Conditional Probability

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

Meaning: Probability of event A **given** B has already occurred.

**Example:**
From a deck of 52 cards:

* Probability of drawing a King = $\frac{4}{52} = \frac{1}{13}$.
* Probability of drawing a King given 1 card already removed (not King) = $\frac{4}{51}$.

---

## 5. Python Example

```python
import random

# Simulation of probability
trials = 100000
success = 0

for _ in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:  # Probability of sum = 7
        success += 1

print("Estimated Probability:", success / trials)
```

---

✅ **Mini Task:**

1. Find the probability of getting at least 1 head in 2 coin tosses.
2. Find the probability of drawing a red card from a deck, given that the first drawn card is also red (without replacement).

---

