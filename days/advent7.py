from typing import List

class Solution:
    def solve(self, textfile: str) -> List:
        with open(textfile) as f:
            data = f.read().splitlines()
        
        validcounter = 0
        passports = [[]]
        passportnr = 0
        for linenr in range(len(data)):          
            if data[linenr] == "":
                passportnr += 1
                passports.append([])
            else:
                to_add = data[linenr].split()              
                passports[passportnr] += [x[:3] for x in to_add]

        for passport in passports:
            if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
                validcounter += 1
        return validcounter

print(Solution().solve(textfile = "adventday3input"))