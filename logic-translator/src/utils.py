
QUANTIFIER_MAP = {
    "all": "∀x", "every": "∀x", "each": "∀x",
    "some": "∃x", "a": "∃x", "an": "∃x",
    "no": "¬∃x", "none": "¬∃x"
}


REVERSE_QUANTIFIER_MAP = {
    "∀x": "All",
    "Vx": "All",  # Handling the 'Vx' format shown in the project hint
    "∃x": "Some",
    "¬∃x": "No",
    "¬∀x": "Not all"
}


CONNECTORS = {
    "and": "∧",
    "or": "∨",
    "implies": "→"
}