from itertools import product
from src.solver import Assignment, _statements, _is_consistent, _has_mixed_group


def build_truth_table() -> list[dict]:

    rows = []

    for combo in product([True, False], repeat=6):
        a = Assignment(*combo)
        stmts = _statements(a)

        row: dict = {}

        # Traveller truth values
        for traveller, value in zip("ABCDEF", a):
            row[traveller] = value

        # Statement evaluations
        for traveller, value in stmts.items():
            row[f"S_{traveller}"] = value

        # Aggregate flags
        row["consistent"] = _is_consistent(a)
        row["mixed"]      = _has_mixed_group(a)
        row["valid"]      = row["consistent"] and row["mixed"]

        rows.append(row)

    return rows



_BOOL = {True: "T", False: "F"}


def print_truth_table(show_all: bool = False) -> None:

    rows = build_truth_table()

    headers = ["A", "B", "C", "D", "E", "F",
               "S_A", "S_B", "S_C", "S_D", "S_E", "S_F",
               "Consistent", "Mixed", "Valid"]

    col_w = [max(len(h), 5) for h in headers]

    separator = "+" + "+".join("-" * (w + 2) for w in col_w) + "+"
    header_row = "|" + "|".join(
        f" {h:^{w}} " for h, w in zip(headers, col_w)
    ) + "|"

    print(separator)
    print(header_row)
    print(separator)

    printed = 0
    for row in rows:
        if not show_all and not row["valid"]:
            continue

        values = (
            [_BOOL[row[k]] for k in "ABCDEF"] +
            [_BOOL[row[f"S_{k}"]] for k in "ABCDEF"] +
            [_BOOL[row["consistent"]], _BOOL[row["mixed"]], _BOOL[row["valid"]]]
        )
        line = "|" + "|".join(
            f" {v:^{w}} " for v, w in zip(values, col_w)
        ) + "|"
        print(line)
        printed += 1

    print(separator)
    label = "valid" if not show_all else "total"
    print(f"\n  {printed} {label} row(s) shown out of 64.\n")


import csv
import io


def truth_table_to_csv() -> str:
    """Return the full 64-row truth table as a CSV string."""
    rows = build_truth_table()
    if not rows:
        return ""

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()
