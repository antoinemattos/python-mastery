# pcost.py

import sys


def calculate_price(file_path):
    cost_for_all_shares = 0.0

    with open(file_path, "r") as f:
        for line in f:
            split_line = line.split()
            cost_for_all_shares += int(split_line[1]) + float(split_line[2])
        print(f"Cost for all shares: {cost_for_all_shares:.2f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: pcost.py path")

    print("pcost.py")
    print(sys.argv)
    print()

    calculate_price(sys.argv[1])
