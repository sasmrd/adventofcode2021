import re
from collections import defaultdict

from input_reader import InputReader


class Day5:

    def __init__(self, file: str):
        self.data = [list(map(int, re.split(' -> |,', x))) for x in InputReader.input_reader_string(file)]
        self.coords = defaultdict(int)

    def part_1(self) -> int:
        for line in self.data:
            x1, y1, x2, y2 = line
            if x1 == x2:
                lower_y = y1 if y1 < y2 else y2
                for j in range(0, abs(y2 - y1) + 1):
                    self.coords[(x1, lower_y + j)] += 1
            elif y1 == y2:
                lower_x = x1 if x1 < x2 else x2
                for i in range(0, abs(x2 - x1) + 1):
                    self.coords[(i + lower_x, y1)] += 1
            else:
                continue
        return sum(x > 1 for x in self.coords.values())

    def part_2(self) -> int:
        for line in self.data:
            x1, y1, x2, y2 = line
            if x1 == x2 or y1 == y2:
                continue
            else:
                [x, y] = [x1, y1]
                direction = [self.sign(x2 - x1), self.sign(y2 - y1)]
                for _ in range(0, abs(x2 - x1) + 1):
                    self.coords[(x, y)] += 1
                    [x, y] = [x + direction[0], y + direction[1]]
        return sum(x > 1 for x in self.coords.values())

    @staticmethod
    def sign(value: int) -> int:
        return 1 if value > 0 else -1


if __name__ == '__main__':
    day5 = Day5('inputs/task5.txt')
    print(day5.data)
    print(day5.part_1())
    print(day5.part_2())
