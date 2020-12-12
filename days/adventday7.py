from typing import List


def read_input(textfile: str) -> List:
    graph = {}
    with open(textfile) as f:
        data = f.read().splitlines()
    for line in data:
        node, connected = line.split(" contain ")
        values = connected[:-1].split(", ")
        graph[node] = {}
        for value in values:
            if value == "no other bags":
                graph[node][value] = 0
            else:
                graph[node][value[2:]] = int(value[:1])
    return graph


def find_upstream_bags(graph, node):
    if "shiny gold bag" in graph[node]:
        return node


def main():
    print(read_input("./inputs/adventday7input"))

    # part_1 = sum([count_yes_per_group(x) for x in read_input("adventday6input")])
    # print(f"The answer to part 1 is: {part_1}")
    # part_2 = sum([count_consensus_yes_per_group(x) for x in read_input("adventday6input")])
    # print(f"The answer to part 2 is: {part_2}")


if __name__ == "__main__":
    main()
