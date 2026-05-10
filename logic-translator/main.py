# main.py
from src.Converter import LogicConverter

def main():
    converter = LogicConverter()
    
    print("="*50)
    print(" MINI PROJECT 2: LOGIC CONVERTER ".center(50))
    print("="*50)

    # Task 1: English to Predicate [cite: 13]
    eng_input_1 = "All dinosaurs are extinct."
    print(f"\n[Task 1] English to Predicate")
    print(f"Input:  \"{eng_input_1}\"")
    print(f"Output: \"{converter.english_to_predicate(eng_input_1)}\"")

    # Task 2: Predicate to English [cite: 16]
    pred_input_2 = "∃x (is_animal(x) ∧ is_endangered(x))"
    print(f"\n[Task 2] Predicate to English")
    print(f"Input:  \"{pred_input_2}\"")
    print(f"Output: \"{converter.predicate_to_english(pred_input_2)}\"")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    main()