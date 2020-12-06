import itertools
from src.input_reader import InputReader


class Day1:

    def __init__(self, file):
        self.data = InputReader.input_reader_int(file)

    @staticmethod
    def part_1(lst, key):
        pairs = [(a, b) for a, b in itertools.permutations(lst, 2) if a + b == key]
        return pairs[0][0] * pairs[0][1]

    @staticmethod
    def part_2(lst, key):
        triples = [(a, b, c) for a, b, c in itertools.permutations(lst, 3) if a + b + c == key]
        return triples[0][0] * triples[0][1] * triples[0][2]


if __name__ == '__main__':
    day1 = Day1('inputs/task1.txt')
    print(day1.data)
    print(day1.part_1(day1.data, 2020))
    print(day1.part_2(day1.data, 2020))
