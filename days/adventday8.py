from typing import List


def parse_input(textfile: str) -> List:
    with open(textfile) as f:
        data = f.read().splitlines()
    bootcode = []
    for line in data:
        operation, argument = line.split()
        bootcode.append([operation, int(argument)])
    return bootcode


def find_loop_acc(bootcode: List) -> int:
    visited_instructions = []
    current_instruction = 0
    accumulator = 0
    while True:
        if current_instruction in visited_instructions:
            return accumulator
        if bootcode[current_instruction][0] == "acc":
            accumulator += bootcode[current_instruction][1]
            visited_instructions.append(current_instruction)
            current_instruction += 1
            continue
        elif bootcode[current_instruction][0] == "jmp":
            visited_instructions.append(current_instruction)
            current_instruction += bootcode[current_instruction][1]
            continue
        elif bootcode[current_instruction][0] == "nop":
            visited_instructions.append(current_instruction)
            current_instruction += 1
            continue
        print("No loop found")
        return


def main():
    part_1 = find_loop_acc(parse_input("../inputs/adventday8input"))
    print(f"The answer to part 1 is: {part_1}")


if __name__ == "__main__":
    main()
