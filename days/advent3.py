from typing import List
from collections import Counter

class Solution:
    def read_input(self, textfile: str) -> List:
        result = list()
        with open(textfile) as file:
            for line in file:
                cleaned_up = line.rstrip("\n")
                result.append(cleaned_up)
        return result



    def find_valid_passwords(self, textfile: str) -> int:
        data = self.read_input(textfile)
        valid_password_counter = 0
        for password in data:
            condition, pw = password.split(': ')
            number, letter = condition.split()
            low, high = number.split('-')
            counted = Counter(pw)
            if int(high) >= counted[letter] >= int(low):
                valid_password_counter += 1
        return valid_password_counter














print(Solution().find_valid_passwords(textfile = "advent3input.txt"))