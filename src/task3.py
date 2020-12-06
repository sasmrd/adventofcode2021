import math
from src.input_reader import InputReader


class Day3:

    def __init__(self, file):
        self.data = InputReader.input_reader_list(file)

    def part_1(self, pair):
        count, across = 0, 0

        for i in range(0, len(self.data), pair[0]):
            down = i
            if across >= 31:
                across -= 31

            if self.data[down][across] == "#":
                count += 1

            across += pair[1]

        return count

    def part_2(self, pairs):
        answers = []
        for pair in pairs:
            answers.append(self.part_1(pair))

        return math.prod(answers)


if __name__ == '__main__':
    day3 = Day3('inputs/task3.txt')
    print(day3.data)
    print(day3.part_1([1, 3]))
    print(day3.part_2([[1, 3], [1, 1], [1, 5], [1, 7], [2, 1]]))
