from typing import List
from itertools import combinations


def parse_input(textfile: str) -> List[int]:
    with open(textfile) as f:
        data = list(map(int, f.read().splitlines()))
    return data


def find_incorrect_number(xmas_data):
    for ix in range(25, len(xmas_data)):
        if xmas_data[ix] not in list(map(sum, combinations(xmas_data[ix - 25:ix], 2))):
            return xmas_data[ix]


def main():
    part_1 = find_incorrect_number(parse_input("../inputs/adventday9input"))
    print(f"The answer to part 1 is: {part_1}")


if __name__ == "__main__":
    main()
