
from src.utils import QUANTIFIER_MAP, REVERSE_QUANTIFIER_MAP, CONNECTORS
from src.parser import create_predicate, extract_predicates

class LogicConverter:
    def __init__(self):
        pass

    def english_to_predicate(self, sentence: str) -> str:
        """Converts an English sentence to Predicate Logic[cite: 7]."""
        sentence = sentence.lower().replace('.', '').strip()
        words = sentence.split()

        if not words:
            return "Error: Empty input."

        quantifier_word = words[0]
        if quantifier_word not in QUANTIFIER_MAP:
            return f"Error: Unsupported quantifier '{quantifier_word}'."

        logic_quantifier = QUANTIFIER_MAP[quantifier_word]

        verb_index = -1
        for i, word in enumerate(words):
            if word in ["are", "is"]:
                verb_index = i
                break

        if verb_index == -1:
            return "Error: Sentence must contain 'is' or 'are'."

        subject_str = " ".join(words[1:verb_index])
        object_str = " ".join(words[verb_index+1:])

        pred_subject = create_predicate(subject_str)
        pred_object = create_predicate(object_str)


        connector = CONNECTORS["implies"] if logic_quantifier == "∀x" else CONNECTORS["and"]

        return f"{logic_quantifier} ({pred_subject} {connector} {pred_object})"

    def predicate_to_english(self, expression: str) -> str:
        """Converts Predicate Logic to an English sentence[cite: 10]."""
        expression = expression.strip()
        

        english_quantifier = None
        for logic_q, eng_q in REVERSE_QUANTIFIER_MAP.items():
            if expression.startswith(logic_q):
                english_quantifier = eng_q
                break
                
        if not english_quantifier:
            return "Error: Unsupported logic quantifier."


        predicates = extract_predicates(expression)
        if len(predicates) != 2:
            return "Error: Expression must contain exactly two 'is_*(x)' predicates."

        subject, obj = predicates[0], predicates[1]


        if not subject.endswith('s') and english_quantifier in ["All", "Some", "No"]:
            subject += "s"

        return f"{english_quantifier} {subject} are {obj}."