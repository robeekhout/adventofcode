from typing import List


def parse_input(textfile: str) -> List[int]:
    with open(textfile) as f:
        data = [int(x) for x in f.read().splitlines()]
        data.sort()
    return data


def chain_the_adapters(adapterlist):
    one_diff = 0
    three_diff = 1  # device's built-in adapter is always three
    adapterlist.insert(0, 0)  # add the charging outlet to the list
    for ix in range(len(adapterlist) - 1):
        if adapterlist[ix + 1] - adapterlist[ix] == 1:
            one_diff += 1
        elif adapterlist[ix + 1] - adapterlist[ix] == 3:
            three_diff += 1
    return one_diff * three_diff


def main():
    part_1 = chain_the_adapters(parse_input("../inputs/adventday10input"))
    print(f"The answer to part 1 is: {part_1}")


if __name__ == "__main__":
    main()
