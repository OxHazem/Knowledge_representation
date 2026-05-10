from itertools import product
from dataclasses import dataclass, field
from typing import Optional




@dataclass(frozen=True)
class Assignment:

    A: bool
    B: bool
    C: bool
    D: bool
    E: bool
    F: bool

    
    def as_dict(self) -> dict[str, bool]:
        """Return {traveller_id: truth_value} mapping."""
        return {k: v for k, v in zip("ABCDEF", self)}

    def __iter__(self):
        return iter((self.A, self.B, self.C, self.D, self.E, self.F))

    def __str__(self) -> str:
        labels = {True: "Truth-teller", False: "Liar"}
        lines = [f"  Traveller {k}: {labels[v]}" for k, v in self.as_dict().items()]
        return "\n".join(lines)



def _statements(a: Assignment) -> dict[str, bool]:
    A, B, C, D, E, F = a

    liar_count = sum(1 for x in (A, B, C, D, E, F) if not x)

    return {
        "A": not B,
        "B": C and D,
        "C": (not A) or (not E),   # A → ¬E
        "D": A == B,                # A ↔ B
        "E": liar_count >= 2,
        "F": D and (not E),
    }


def _is_consistent(a: Assignment) -> bool:

    stmts = _statements(a)
    for traveller, truth_value in a.as_dict().items():
        if truth_value != stmts[traveller]:
            return False
    return True


def _has_mixed_group(a: Assignment) -> bool:
    
    values = list(a)
    return any(values) and not all(values)



def solve() -> list[Assignment]:

    solutions: list[Assignment] = []

    for combo in product([True, False], repeat=6):
        a = Assignment(*combo)
        if _is_consistent(a) and _has_mixed_group(a):
            solutions.append(a)

    return solutions


def get_statements_table() -> list[dict]:

    return [
        {
            "traveller": "A",
            "natural":   "Traveller B is lying.",
            "logic":     "S_A = ¬B",
        },
        {
            "traveller": "B",
            "natural":   "Traveller C and D are both truth-tellers.",
            "logic":     "S_B = C ∧ D",
        },
        {
            "traveller": "C",
            "natural":   "If A is truthful, then E is lying.",
            "logic":     "S_C = A → ¬E  ≡  ¬A ∨ ¬E",
        },
        {
            "traveller": "D",
            "natural":   "Traveller A and B are either both truthful or both lying.",
            "logic":     "S_D = A ↔ B",
        },
        {
            "traveller": "E",
            "natural":   "At least two of us are lying.",
            "logic":     "S_E = |{X : ¬X}| ≥ 2",
        },
        {
            "traveller": "F",
            "natural":   "Traveller D is truthful, and Traveller E is lying.",
            "logic":     "S_F = D ∧ ¬E",
        },
    ]
