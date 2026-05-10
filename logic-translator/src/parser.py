
import re

def create_predicate(word: str) -> str:
    """Converts a word like 'dinosaurs' into 'is_dinosaur(x)'."""
    word = word.lower().strip()
   
    if word.endswith('s') and len(word) > 3:
        word = word[:-1]
    return f"is_{word}(x)"

def extract_predicates(expression: str) -> list:
    # Matches any text between 'is_' and '(x)'
    matches = re.findall(r'is_([a-zA-Z_]+)\(x\)', expression)
    return matches