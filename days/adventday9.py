from itertools import combinations

from typing import List


def parse_input(textfile: str) -> List[int]:
    with open(textfile) as f:
        data = list(map(int, f.read().splitlines()))
    return data


def find_incorrect_number(xmas_data: list) -> int:
    for ix in range(25, len(xmas_data)):
        if xmas_data[ix] not in list(map(sum, combinations(xmas_data[ix - 25:ix], 2))):
            return xmas_data[ix]


def find_encryption_weakness(xmas_data: List[int], invalid_number: int) -> int:
    for ix in range(len(xmas_data)):
        running_sum = 0
        running_ix = ix
        while running_sum <= invalid_number:
            if running_sum == invalid_number:
                return min(xmas_data[ix:running_ix + 1]) + max(xmas_data[ix:running_ix + 1])
            else:
                running_sum += xmas_data[running_ix]
                running_ix += 1


def main():
    part_1 = find_incorrect_number(parse_input("../inputs/adventday9input"))
    print(f"The answer to part 1 is: {part_1}")
    part_2 = find_encryption_weakness(parse_input("../inputs/adventday9input"), part_1)
    print(f"The answer to part 2 is: {part_2}")


if __name__ == "__main__":
    main()
