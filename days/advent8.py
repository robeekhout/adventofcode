from typing import List
import re

class Solution:
    def solve(self, textfile: str) -> List:
        with open(textfile) as f:
            data = f.read().splitlines()
        
        validcounter = 0
        passports = [{}]
        passportnr = 0
        for linenr in range(len(data)):          
            if data[linenr] == "":
                passportnr += 1
                passports.append({})
            else:   
                to_add = data[linenr].split()
                for kvp in to_add:
                    passports[passportnr][kvp.split(":")[0]] = kvp.split(":")[1]

        for passport in passports:
            if self.check_conditions(passport) == True:
                validcounter += 1        
        return validcounter


    def check_conditions(self, passport):
        if "byr" not in passport or "iyr" not in passport or "eyr" not in passport or "hgt" not in passport or "hcl" not in passport or "ecl" not in passport or "pid" not in passport:
            return False
        if int(passport["byr"]) not in range(1920, 2003):
            return False
        if int(passport["iyr"]) not in range(2010, 2021):
            return False
        if int(passport["eyr"]) not in range(2020, 2031):
            return False
        if not re.match(r"^[0-9]+((cm)|(in))$", passport["hgt"]):
            return False
        if passport["hgt"][-2:] == "cm" and int(passport["hgt"][:-2]) not in range(150,194):
                return False
        if passport["hgt"][-2:] == "in" and int(passport["hgt"][:-2]) not in range(59,77):
                return False
        if not re.match(r"^#[a-f0-9]{6}$", passport["hcl"]):
            return False
        if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            return False
        if not re.match(r"^[0-9]{9}$", passport["pid"]):
            return False  
        return True

print(Solution().solve(textfile = "adventday3input"))