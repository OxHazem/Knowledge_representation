# 🏛️ Labyrinth of Truth and Lies — Propositional Logic Solver

> **DSAI104 · Knowledge Representation and Reasoning**  
> University of Science and Technology — School of Computational Science and AI

A clean, well-tested Python solver for the *Labyrinth of Truth and Lies* puzzle.  
Given six travellers whose statements may be true or false, the solver finds every  
self-consistent truth assignment that satisfies all propositional logic constraints  
and identifies the **unique escape condition** that opens the magical door.

---

## 📋 Table of Contents

- [Problem Statement](#-problem-statement)
- [Propositional Logic Encoding](#-propositional-logic-encoding)
- [Solution & Escape Condition](#-solution--escape-condition)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Running the Tests](#-running-the-tests)
- [How It Works](#-how-it-works)

---

## 🧩 Problem Statement

Six travellers — **A, B, C, D, E, F** — are trapped in a labyrinth.  
Each traveller either *always tells the truth* or *always lies*.  
A door opens only when the correct truth-assignment satisfies all logical constraints.

**Rules:**
1. Each traveller makes exactly one statement.
2. A truth-teller's statement is always **True**; a liar's statement is always **False**.
3. There is **at least one liar** and **at least one truth-teller** in the group.

**Statements:**

| Traveller | Statement |
|-----------|-----------|
| A | "Traveller B is lying." |
| B | "Traveller C and D are both truth-tellers." |
| C | "If A is truthful, then E is lying." |
| D | "Traveller A and B are either both truthful or both lying." |
| E | "At least two of us are lying." |
| F | "Traveller D is truthful, and Traveller E is lying." |

---

## 🔣 Propositional Logic Encoding

Let each variable **A, B, C, D, E, F ∈ {T, F}** represent whether that traveller is a truth-teller (`True`) or a liar (`False`).

Each statement is encoded as a Boolean formula **S_X**. Consistency requires:

> **∀ X ∈ {A,…,F} : X ↔ S_X(A,…,F)**

| Traveller | Statement Formula | Notes |
|-----------|------------------|-------|
| A | `S_A = ¬B` | A says B lies |
| B | `S_B = C ∧ D` | B says both C and D are truthful |
| C | `S_C = A → ¬E ≡ ¬A ∨ ¬E` | C makes a conditional claim |
| D | `S_D = A ↔ B` | D says A and B have the same truth value |
| E | `S_E = \|{X : ¬X}\| ≥ 2` | E claims at least 2 liars exist |
| F | `S_F = D ∧ ¬E` | F makes a conjunction claim |

---

## 🚪 Solution & Escape Condition

The solver checks all **2⁶ = 64** possible assignments and finds **exactly one** that satisfies all constraints:

| Traveller | Role |
|-----------|------|
| **A** | ✅ Truth-teller |
| **B** | ❌ Liar |
| **C** | ❌ Liar |
| **D** | ❌ Liar |
| **E** | ✅ Truth-teller |
| **F** | ❌ Liar |

**Verification:**

| Check | Statement | Value | Matches Role? |
|-------|-----------|-------|---------------|
| S_A = ¬B | ¬False = True | True | ✅ A is truthful |
| S_B = C ∧ D | False ∧ False = False | False | ✅ B is lying |
| S_C = ¬A ∨ ¬E | ¬True ∨ ¬True = False | False | ✅ C is lying |
| S_D = A ↔ B | True ↔ False = False | False | ✅ D is lying |
| S_E = liars ≥ 2 | 4 liars ≥ 2 = True | True | ✅ E is truthful |
| S_F = D ∧ ¬E | False ∧ False = False | False | ✅ F is lying |

**The door opens. 🚪**

---

## 📁 Project Structure

```
labyrinth-solver/
│
├── src/
│   ├── __init__.py          # Public package API
│   ├── solver.py            # Core logic: Assignment, constraints, solver
│   └── truth_table.py       # 64-row truth table builder + CSV export
│
├── tests/
│   ├── conftest.py          # pytest path setup
│   └── test_solver.py       # Unit tests for solver + truth table
│
├── docs/
│   └── logic_derivation.md  # Step-by-step logical reasoning
│
├── main.py                  # CLI entry point
├── requirements.txt         # Dependencies
└── README.md
```

---

## ⚡ Quick Start

```bash
# Clone and enter
git clone https://github.com/your-username/labyrinth-solver.git
cd labyrinth-solver

# No external dependencies required for the solver itself
python main.py
```

---

## 🖥️ Usage

```bash
# Solve the puzzle (default — shows everything)
python main.py

# Show propositional logic encodings only
python main.py --statements

# Print the truth table (valid rows only)
python main.py --table

# Print all 64 rows of the truth table
python main.py --table --all

# Export the full truth table to CSV
python main.py --export csv
```

---

## 🧪 Running the Tests

```bash
# Install pytest
pip install pytest

# Run all tests with verbose output
pytest tests/ -v
```

The test suite covers:
- Unique solution existence
- Correct truth values for each traveller
- Mixed-group constraint enforcement
- Individual statement formula correctness
- Truth table row count (64) and valid row count (1)
- CSV export shape and column presence

---

## ⚙️ How It Works

The solver uses **brute-force enumeration** — appropriate for a 6-variable problem with only 64 possible assignments.

```
for every (A, B, C, D, E, F) ∈ {T, F}⁶:
    evaluate S_A … S_F
    if ∀ X : (X ↔ S_X)   ← self-consistency
    and ∃ truth-teller and ∃ liar   ← Rule 3
    then: valid solution found
```

**Complexity:** O(2ⁿ) where n = 6 → 64 iterations. Instantaneous.

For larger puzzles, a SAT-solver backend (e.g. `pysat`, `z3`) could be substituted with no changes to the public API.

---

## 📄 License

MIT — see `LICENSE` for details.