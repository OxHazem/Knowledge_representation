
import unittest
from src.Converter import LogicConverter

class TestEnglishToPredicate(unittest.TestCase):
    def setUp(self):
        self.converter = LogicConverter()

    def test_universal_quantifier(self):
        # Testing the exact project example [cite: 14, 15]
        result = self.converter.english_to_predicate("All dinosaurs are extinct.")
        self.assertEqual(result, "∀x (is_dinosaur(x) → is_extinct(x))")

    def test_existential_quantifier(self):
        result = self.converter.english_to_predicate("Some animals are endangered.")
        self.assertEqual(result, "∃x (is_animal(x) ∧ is_endangered(x))")

if __name__ == "__main__":
    unittest.main()