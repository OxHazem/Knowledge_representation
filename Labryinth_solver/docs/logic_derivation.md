# Logical Derivation — Step-by-Step

This document walks through the manual reasoning process that leads to the unique escape condition.

---

## Setup

Let **T** denote *truth-teller* and **F** denote *liar*.  
Each assignment must satisfy:  traveller X's truth value ↔ X's statement evaluates to True.

Encoded constraints:

```
(1)  A ↔ ¬B          (A says B lies)
(2)  B ↔ (C ∧ D)     (B says both C and D are truthful)
(3)  C ↔ (¬A ∨ ¬E)  (C: if A truthful then E lies)
(4)  D ↔ (A ↔ B)    (D says A and B share same value)
(5)  E ↔ (liars ≥ 2)
(6)  F ↔ (D ∧ ¬E)   (F says D truthful and E lies)
```

Plus Rule 3: not all T, not all F.

---

## Derivation

### Step 1 — Constraint (1): A ↔ ¬B

This is a biconditional.  Two cases exist:

- **Case α:** A = T, B = F
- **Case β:** A = F, B = T

We explore each.

---

### Case α: A = T, B = F

From (2): B ↔ (C ∧ D)  
B = F, so statement must be False → C ∧ D = False → **at least one of C, D is False**.

From (4): D ↔ (A ↔ B) = (T ↔ F) = False  
So statement is False → D = F. ✓ (consistent with C ∧ D = False)

From (1): confirmed A = T, B = F.

From (3): C ↔ (¬A ∨ ¬E) = (F ∨ ¬E) = ¬E  
So C ↔ ¬E.

From (6): F ↔ (D ∧ ¬E) = (F ∧ ¬E) = False  
So F's statement is False → **F = F** (liar).

Now determine C and E using C ↔ ¬E:

- **Sub-case α1:** C = T, E = F  
  Liars = {B, D, F} → 3 liars.  
  Statement E: "at least 2 lying" = True.  
  But E = F means E's statement must be False. Contradiction. ✗

- **Sub-case α2:** C = F, E = T  
  Liars = {B, C, D, F} → 4 liars.  
  Statement E: "at least 2 lying" = True.  
  E = T means E's statement must be True. ✓  
  
  **Full assignment: A=T, B=F, C=F, D=F, E=T, F=F** ✓

---

### Case β: A = F, B = T

From (2): B = T, so statement must be True → C ∧ D = True → **C = T and D = T**.

From (4): D ↔ (A ↔ B) = (F ↔ T) = False  
Statement is False → D = F.  
But we just derived D = T. **Contradiction.** ✗

Case β yields no valid assignment.

---

## Conclusion

The **unique** valid assignment is:

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| T | F | F | F | T | F |

**Truth-tellers:** A, E  
**Liars:** B, C, D, F  

This is the only assignment consistent with all six propositional constraints and Rule 3 (mixed group). The door opens.