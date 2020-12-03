from typing import List

class Solution:
    def read_input(self, textfile: str) -> List:
        result = list()
        with open(textfile) as file:
            for line in file:
                cleaned_up = line.rstrip("\n")
                result.append(cleaned_up)
        return result

    def find_trees(self, textfile: str, down, right) -> int:
        data = self.read_input(textfile)
        treecounter = 0
        indexcounter = right
        for line in range(down, len(data), down):
            if data[line][indexcounter] == "#":
                treecounter += 1
            indexcounter += right
            if indexcounter >= len(data[indexcounter]):
                indexcounter %= len(data[indexcounter])
        return treecounter


print(Solution().find_trees(textfile = "advent5input.txt", down = 1, right = 1) * Solution().find_trees(textfile = "advent5input.txt", down = 1, right = 3) * Solution().find_trees(textfile = "advent5input.txt", down = 1, right = 5) * Solution().find_trees(textfile = "advent5input.txt", down = 1, right = 7) * Solution().find_trees(textfile = "advent5input.txt", down = 2, right = 1))
