# test/test_pred_to_en.py
import unittest
from src.Converter import LogicConverter

class TestPredicateToEnglish(unittest.TestCase):
    def setUp(self):
        self.converter = LogicConverter()

    def test_existential_conversion(self):
        # Testing the exact project hint [cite: 18, 19]
        # Note: Using ∧ instead of 'A' for accuracy
        result = self.converter.predicate_to_english("∃x (is_animal(x) ∧ is_endangered(x))")
        self.assertEqual(result, "Some animals are endangered.")

    def test_universal_conversion(self):
        result = self.converter.predicate_to_english("∀x (is_dinosaur(x) → is_extinct(x))")
        self.assertEqual(result, "All dinosaurs are extinct.")

if __name__ == "__main__":
    unittest.main()