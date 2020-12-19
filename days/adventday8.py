from typing import List
from collections import Counter


def parse_input(textfile: str) -> List:
    with open(textfile) as f:
        data = f.read().splitlines()
    bootcode = []
    for line in data:
        operation, argument = line.split()
        bootcode.append([operation, int(argument)])
    return bootcode

def find_loop_acc(bootcode: List):
    current_instruction = 0
    while True:



def main():
    # part_1 = sum([count_yes_per_group(x) for x in read_input("./inputs/adventday6input")])
    # print(f"The answer to part 1 is: {part_1}")
    # part_2 = sum([count_consensus_yes_per_group(x) for x in read_input("./inputs/adventday6input")])
    # print(f"The answer to part 2 is: {part_2}")
    print(read_input("../inputs/adventday8input"))


if __name__ == "__main__":
    main()
