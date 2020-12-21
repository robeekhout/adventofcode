def parse_input(textfile: str) -> tuple:
    with open(textfile) as f:
        earliest = int(f.readline().rstrip("\n"))
        bus_ids = [int(x) for x in f.readline().rstrip("\n").split(",") if x != "x"]
    return earliest, bus_ids


def find_earliest_bus(earliest, bus_ids):
    lowest_wait_time = 99999
    optimal_bus_id = 0
    for id in bus_ids:
        wait_time = id - (earliest % id)
        if wait_time < lowest_wait_time:
            lowest_wait_time = wait_time
            optimal_bus_id = id
    return optimal_bus_id * lowest_wait_time


def main():
    print(parse_input("../inputs/adventday13input"))
    part_1 = find_earliest_bus(*parse_input("../inputs/adventday13input"))
    print(f"The answer to part 1 is: {part_1}")


if __name__ == "__main__":
    main()
