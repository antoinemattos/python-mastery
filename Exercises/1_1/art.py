# art.py

import sys
import random

chars = "\|/"


def draw(rows, columns):
    for _ in range(rows):
        print("".join(random.choice(chars) for _ in range(columns)))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py rows columns")

    print("art.py")
    print(f"argv[0] {sys.argv[0]}")
    print(f"argv[1] {sys.argv[1]}")
    print(f"argv[2] {sys.argv[2]}")
    print()

    draw(int(sys.argv[1]), int(sys.argv[2]))
