from typing import List
from collections import Counter


def read_input(textfile: str) -> List:
    groups = [[]]
    groupnr = 0
    with open(textfile) as f:
        data = f.read().splitlines()
    for linenr in range(len(data)):
        if data[linenr] == "":
            groupnr += 1
            groups.append([])
        else:
            groups[groupnr].append(list(data[linenr]))
    return groups


def count_yes_per_group(group: List) -> int:
    all_questions_with_yes = set()
    for person in group:
        for question in person:
            all_questions_with_yes.add(question)
    return len(all_questions_with_yes)


def count_consensus_yes_per_group(group: List) -> int:
    result = 0
    counted = Counter()
    for person in group:
        counted += Counter(person)
    for key in counted:
        if counted[key] == len(group):
            result += 1
    return result


def main():
    part_1 = sum([count_yes_per_group(x) for x in read_input("./inputs/adventday6input")])
    print(f"The answer to part 1 is: {part_1}")
    part_2 = sum([count_consensus_yes_per_group(x) for x in read_input("./inputs/adventday6input")])
    print(f"The answer to part 2 is: {part_2}")


if __name__ == "__main__":
    main()
