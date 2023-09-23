# pcost.py

import sys


def portfolio_cost(filename):
    cost_for_all_shares = 0.0

    with open(filename, "r") as f:
        for line in f:
            try:
                split_line = line.split()
                cost_for_all_shares += int(split_line[1]) * float(split_line[2])
            except ValueError as valueError:
                print(f"Couldn't parse: '{line.strip()}'")
                print(f"Reason: {valueError}\n")
        return cost_for_all_shares


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: pcost.py path")

    print("pcost.py")
    print(sys.argv)
    print()

    print(f"Cost for all shares: {portfolio_cost(sys.argv[1]):.2f}")
