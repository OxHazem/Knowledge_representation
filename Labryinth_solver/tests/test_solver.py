import pytest
from src.solver      import solve, Assignment, _statements, _is_consistent, _has_mixed_group
from src.truth_table import build_truth_table, truth_table_to_csv



@pytest.fixture
def unique_solution() -> Assignment:
    solutions = solve()
    assert len(solutions) == 1, "Expected exactly one solution."
    return solutions[0]

class TestSolver:
    def test_unique_solution_exists(self):
        """The puzzle must have exactly one valid assignment."""
        solutions = solve()
        assert len(solutions) == 1

    def test_correct_truth_values(self, unique_solution):
        """Verify the expected truth assignment matches the known answer."""
        sol = unique_solution.as_dict()
        assert sol["A"] is True,  "A should be a truth-teller"
        assert sol["B"] is False, "B should be a liar"
        assert sol["C"] is False, "C should be a liar"
        assert sol["D"] is False, "D should be a liar"
        assert sol["E"] is True,  "E should be a truth-teller"
        assert sol["F"] is False, "F should be a liar"

    def test_mixed_group_rule(self, unique_solution):
        """Solution must contain at least one truth-teller and one liar."""
        values = list(unique_solution)
        assert any(values),      "Must have at least one truth-teller"
        assert not all(values),  "Must have at least one liar"

    def test_self_consistency(self, unique_solution):
        """Every traveller's truth value must match their statement."""
        assert _is_consistent(unique_solution)

    def test_all_liars_rejected(self):
        """A group of all liars is invalid (violates Rule 3)."""
        a = Assignment(False, False, False, False, False, False)
        assert not _has_mixed_group(a)

    def test_all_truthtellers_rejected(self):
        """A group of all truth-tellers is invalid (violates Rule 3)."""
        a = Assignment(True, True, True, True, True, True)
        assert not _has_mixed_group(a)



class TestStatements:
    def test_statement_A_truth(self):
        """S_A = ¬B.  When B is False, S_A should be True."""
        a = Assignment(True, False, True, True, False, False)
        assert _statements(a)["A"] is True

    def test_statement_A_lie(self):
        """S_A = ¬B.  When B is True, S_A should be False."""
        a = Assignment(False, True, True, True, False, False)
        assert _statements(a)["A"] is False

    def test_statement_B(self):
        """S_B = C ∧ D."""
        # Both truth-tellers → True
        a = Assignment(False, True, True, True, False, False)
        assert _statements(a)["B"] is True
        # Only C → False
        b = Assignment(False, True, True, False, False, False)
        assert _statements(b)["B"] is False

    def test_statement_C_implication(self):
        """S_C = A → ¬E.  False antecedent makes implication True."""
        a = Assignment(False, False, True, False, True, False)
        assert _statements(a)["C"] is True   # A=False → implication vacuously True

    def test_statement_D_biconditional(self):
        """S_D = A ↔ B."""
        a = Assignment(True, True, False, True, False, False)
        assert _statements(a)["D"] is True
        b = Assignment(True, False, False, True, False, False)
        assert _statements(b)["D"] is False

    def test_statement_E_liar_count(self):
        """S_E is True iff at least 2 travellers are liars."""
        # 4 liars → True
        a = Assignment(True, False, False, False, True, False)
        assert _statements(a)["E"] is True
        # 0 liars → False
        b = Assignment(True, True, True, True, True, True)
        assert _statements(b)["E"] is False

    def test_statement_F(self):
        """S_F = D ∧ ¬E."""
        a = Assignment(False, False, False, True, False, True)
        assert _statements(a)["F"] is True
        b = Assignment(False, False, False, True, True, True)
        assert _statements(b)["F"] is False



class TestTruthTable:
    def test_row_count(self):
        """Truth table must have exactly 64 rows (2^6)."""
        rows = build_truth_table()
        assert len(rows) == 64

    def test_valid_rows(self):
        """Exactly one row should be marked valid."""
        rows = build_truth_table()
        valid = [r for r in rows if r["valid"]]
        assert len(valid) == 1

    def test_csv_row_count(self):
        """CSV export should have 64 data rows + 1 header."""
        csv_text = truth_table_to_csv()
        lines = [l for l in csv_text.strip().splitlines() if l]
        assert len(lines) == 65   # header + 64 rows

    def test_csv_columns(self):
        """CSV must include all traveller, statement, and flag columns."""
        csv_text = truth_table_to_csv()
        header = csv_text.splitlines()[0]
        for col in ["A", "B", "C", "D", "E", "F",
                    "S_A", "S_B", "S_C", "S_D", "S_E", "S_F",
                    "consistent", "mixed", "valid"]:
            assert col in header, f"Column '{col}' missing from CSV header"
