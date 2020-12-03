from typing import List

class Solution:
    def read_input(self, textfile: str) -> List:
        result = list()
        with open(textfile) as file:
            for line in file:
                cleaned_up = line.rstrip("\n")
                result.append(cleaned_up)
        return result

    def find_trees(self, textfile: str) -> int:
        data = self.read_input(textfile)
        treecounter = 0
        indexcounter = 3
        for line in range(1, len(data)):
            if data[line][indexcounter] == "#":
                treecounter += 1
            indexcounter += 3
            if indexcounter >= len(data[indexcounter]):
                indexcounter %= len(data[indexcounter])
        return treecounter


print(Solution().find_trees(textfile = "advent5input.txt"))