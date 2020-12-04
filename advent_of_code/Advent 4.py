import re

f = open("input4.txt", "r")
passports = f.read().split('\n\n')
passports = [passport.replace('\n', ' ') for passport in passports]
results = []

# Task 1
for passport in passports:
    results.append(re.match("(?=.*iyr)(?=.*byr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid)", passport))
print(f'Task1: {sum(x is not None for x in results)}')


class Passport:
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None

    def is_valid_byr(self, low, high):
        return self.byr is not None and low <= int(self.byr) <= high

    def is_valid_iyr(self, low, high):
        return self.iyr is not None and low <= int(self.iyr) <= high

    def is_valid_eyr(self, low, high):
        return self.eyr is not None and low <= int(self.eyr) <= high

    def is_valid_hgt(self):
        if self.hgt is None:
            return False
        if 'cm' in self.hgt:
            return 150 <= int(self.hgt.strip('cm')) <= 193
        elif 'in' in self.hgt:
            return 59 <= int(self.hgt.strip('in')) <= 76

    def is_valid_hcl(self):
        return self.hcl is not None

    def is_valid_pid(self):
        return self.pid is not None

    def is_valid_ecl(self):
        return self.ecl is not None


pps = []
count = 0
for passport in passports:
    pp = Passport()
    pp.byr = re.search(r"(?<=byr:)[0-9]{4}", passport).group(0) if re.search(r"(?<=byr:)[0-9]{4}", passport) else None
    pp.iyr = re.search(r"(?<=iyr:)[0-9]{4}", passport).group(0) if re.search(r"(?<=iyr:)[0-9]{4}", passport) else None
    pp.eyr = re.search(r"(?<=eyr:)[0-9]{4}", passport).group(0) if re.search(r"(?<=eyr:)[0-9]{4}", passport) else None
    pp.hgt = re.search(r"(?<=hgt:)[0-9]+[\w]{2}", passport).group(0) if re.search(r"(?<=hgt:)[0-9]+[\w]{2}", passport) else None
    pp.hcl = re.search(r"(?<=hcl:)#[0-9 a-f]{6}", passport).group(0) if re.search(r"(?<=hcl:)#[0-9 a-f]{6}", passport) else None
    pp.ecl = re.search(r"(?<=ecl:)amb|blu|brn|gry|grn|hzl|oth", passport).group(0) \
        if re.search(r"(?<=ecl:)amb|blu|brn|gry|grn|hzl|oth", passport) else None
    pp.pid = re.search(r"(?<!\d)\d{9}(?!\d)", passport).group(0) if re.search(r"(?<!\d)\d{9}(?!\d)", passport) else None
    if pp.is_valid_byr(1920, 2002) and pp.is_valid_iyr(2010, 2020) and pp.is_valid_eyr(2020, 2030) and pp.is_valid_ecl() \
            and pp.is_valid_hcl() and pp.is_valid_hgt() and pp.is_valid_pid():
        count += 1

print(f'Task2: {count}')




