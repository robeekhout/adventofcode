from typing import List


def parse_input(textfile: str) -> List[int]:
    with open(textfile) as f:
        data = [int(x) for x in f.read().splitlines()]
        data.sort()
    return data

def chain_the_adapters(adapterlist):
    #solve pt1
    return


def main():
    print(parse_input("../inputs/adventday10input"))
    # part_1 = find_incorrect_number(parse_input("../inputs/adventday9input"))
    # print(f"The answer to part 1 is: {part_1}")
    # part_2 = find_encryption_weakness(parse_input("../inputs/adventday9input"), part_1)
    # print(f"The answer to part 2 is: {part_2}")


if __name__ == "__main__":
    main()
