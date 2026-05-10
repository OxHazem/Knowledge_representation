
import argparse
import sys
import csv

from src.solver      import solve, get_statements_table
from src.truth_table import print_truth_table, truth_table_to_csv


DIVIDER = "=" * 62
THIN    = "-" * 62


def _header(title: str) -> None:
    print(f"\n{DIVIDER}")
    print(f"  {title}")
    print(DIVIDER)


def _show_statements() -> None:
    _header("Propositional Logic Encoding")
    table = get_statements_table()
    for row in table:
        print(f"\n  Traveller {row['traveller']}")
        print(f"    Statement : {row['natural']}")
        print(f"    Formula   : {row['logic']}")
    print()


def _show_solution() -> None:
    _header("Solving the Labyrinth …")

    solutions = solve()

    if not solutions:
        print("\n  ✗  No valid assignment found.")
        print("     The door remains shut.\n")
        sys.exit(1)

    print(f"\n  Found {len(solutions)} valid assignment(s).\n")

    for i, sol in enumerate(solutions, 1):
        print(f"  ── Solution {i} {'(Unique Escape Condition)' if len(solutions) == 1 else ''} ──")
        print(sol)
        print()

    if len(solutions) == 1:
        _header("Escape Condition Analysis")
        sol = solutions[0]
        d = sol.as_dict()
        truth_tellers = [k for k, v in d.items() if v]
        liars         = [k for k, v in d.items() if not v]
        print(f"\n  Truth-tellers : {', '.join(truth_tellers)}")
        print(f"  Liars         : {', '.join(liars)}")
        print(f"\n  The door opens for this unique configuration.")
        print(f"  No other assignment of truth values is consistent.\n")



def main() -> None:
    parser = argparse.ArgumentParser(
        prog="labyrinth-solver",
        description="Propositional Logic Solver — Labyrinth of Truth and Lies",
    )
    parser.add_argument(
        "--statements", action="store_true",
        help="Display the propositional logic encodings of each statement."
    )
    parser.add_argument(
        "--table", action="store_true",
        help="Print the truth table (valid rows only by default)."
    )
    parser.add_argument(
        "--all", dest="show_all", action="store_true",
        help="When used with --table, print all 64 rows."
    )
    parser.add_argument(
        "--export", choices=["csv"], metavar="FORMAT",
        help="Export the full truth table. Supported: csv"
    )

    args = parser.parse_args()

    # Default behaviour: show everything
    if not any([args.statements, args.table, args.export]):
        _show_statements()
        _show_solution()
        return

    if args.statements:
        _show_statements()

    if args.table:
        _header("Truth Table" + (" (all rows)" if args.show_all else " (valid rows only)"))
        print_truth_table(show_all=args.show_all)

    if args.export == "csv":
        path = "truth_table.csv"
        with open(path, "w", newline="") as f:
            f.write(truth_table_to_csv())
        print(f"\n  ✓  Truth table exported to '{path}'  (64 rows)\n")

    # Always solve unless only --export was requested with no other flags
    if args.statements or args.table:
        _show_solution()


if __name__ == "__main__":
    main()
