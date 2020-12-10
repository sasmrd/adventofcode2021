import itertools
from src.input_reader import InputReader


class Day9:

    def __init__(self, file):
        self.data = InputReader.input_reader_int(file)

    def part_1(self, length):
        for index, entry in enumerate(self.data):
            preamble = self.data[index:index+length]
            pairs = self.get_pairs(preamble, self.data[index+length])
            if len(pairs) == 0:
                return self.data[index+length]

    def part_2(self, number):
        index = self.data.index(number)
        lst = self.data.copy()[:index]
        for element in self.data[:index]:
            small, big = self.find_contiguous_set(element, lst, number)
            if big == 0:
                lst = lst[1:]
            else:
                break
        return small + big

    @staticmethod
    def set_up(preamble_length, lst):
        preamble = lst[:preamble_length]
        inputs = lst[preamble_length:]
        return preamble, inputs

    @staticmethod
    def get_pairs(lst, key):
        return [(a, b) for a, b in itertools.combinations(lst, 2) if a + b == key]

    @staticmethod
    def find_contiguous_set(start, lst, target):
        total = 0
        for each in lst:
            total += each
            if total == target:
                return min(lst[lst.index(start):lst.index(each)+1]), max(lst[lst.index(start):lst.index(each)+1])
            if total > target:
                return start, 0


if __name__ == '__main__':
    day9 = Day9('inputs/task9.txt')
    num = day9.part_1(25)
    print("Part 1:", num)
    print("Part 2:", day9.part_2(num))
