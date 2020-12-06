import re
from src.input_reader import InputReader


def byr(value):
    try:
        return 1920 <= int(value) <= 2002
    except ValueError:
        return False


def iyr(value):
    try:
        return 2010 <= int(value) <= 2020
    except ValueError:
        return False


def eyr(value):
    try:
        return 2020 <= int(value) <= 2030
    except ValueError:
        return False


def hgt(value):
    try:
        if value.endswith("cm"):
            return 150 <= int(value[:-2]) <= 193
        elif value.endswith("in"):
            return 59 <= int(value[:-2]) <= 76
    except ValueError:
        return False


def hcl(value):
    return re.compile(r'^#[0-9a-f]{6}$').match(value)


def ecl(value):
    poss = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if value not in poss:
        return False
    else:
        return True


def pid(value):
    if len(value) != 9:
        return False
    else:
        return 0 <= int(value) <= 999999999


class Day4:

    def __init__(self, file):
        self.data = InputReader.input_reader_string_blank_lines(file)

    REQ = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    REQ_FUNC = [byr, iyr, eyr, hgt, hcl, ecl, pid]

    def part_1(self):
        valid = 0
        for passport in self.data:
            if self.any_missing_fields(passport):
                valid += 1

        return valid

    def part_2(self):
        valid = 0
        for passport in self.data:
            if self.any_missing_fields(passport) and self.all_fields_valid(passport):
                valid += 1
        return valid

    def any_missing_fields(self, passport) -> bool:
        for field in self.REQ:
            if field not in passport:
                return False
        return True

    def all_fields_valid(self, passport) -> bool:
        pairs = passport.split()
        invalid_fields = []
        for each in pairs:
            try:
                index = self.REQ.index(each[:4])
            except ValueError:
                continue
            else:
                if not self.REQ_FUNC[index](each[4:]):
                    invalid_fields.append(each[:3])
        return len(invalid_fields) == 0


if __name__ == '__main__':
    day4 = Day4('inputs/task4.txt')
    print(day4.data)
    print(day4.part_1())
    print(day4.part_2())
