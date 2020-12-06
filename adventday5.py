from typing import List


def read_input(textfile: str) -> List:
    with open(textfile) as f:
        data = f.read().splitlines()
    return data


def find_seat(seat: str) -> int:
    high_row = 127
    low_row = 0
    high_column = 7
    low_column = 0
    for char in seat:
        if char == "F":
            high_row = (high_row + low_row) // 2
        elif char == "B":
            low_row = (high_row + low_row) // 2 + 1
        elif char == "R":
            low_column = (high_column + low_column) // 2 + 1
        elif char == "L":
            high_column = (high_column + low_column) // 2
    row = low_row
    column = low_column
    seat_id = (row * 8) + column
    return seat_id


def main():
    all_seat_ids = sorted([find_seat(x) for x in read_input("adventday5input")])
    part_1 = max(all_seat_ids)
    print(f"The answer to part 1 is: {part_1}")
    part_2 = sum(range(all_seat_ids[0], all_seat_ids[-1] + 1)) - sum(all_seat_ids)
    print(f"The answer to part 2 is: {part_2}")


if __name__ == "__main__":
    main()
