from input_reader import InputReader


class Day1:

    def __init__(self, file):
        self.data = InputReader.input_reader_int(file)

    def part_1(self):
        return sum(1 if self.data[i + 1] > self.data[i] else 0 for i in range(0, len(self.data)-1))

    def part_2(self):
        return sum(1 if sum(self.data[i+1:i+4]) > sum(self.data[i:i+3]) else 0 for i in range(0, len(self.data)-3))


if __name__ == '__main__':
    day1 = Day1('inputs/task1.txt')
    print(day1.data)
    print(day1.part_1())
    print(day1.part_2())
