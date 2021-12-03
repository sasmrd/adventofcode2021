from input_reader import InputReader


class Day1:

    def __init__(self, file):
        self.data = InputReader.input_reader_int(file)

    def part_1(self):
        count = 0
        before = 100000
        for depth in self.data:
            if depth > before:
                count += 1
            before = depth
        return count

    def part_2(self):
        count = 0
        prev = 100000000
        for i in range(0, len(self.data) - 2):
            total = self.data[i] + self.data[i + 1] + self.data[i + 2]
            if total > prev:
                count += 1
            prev = total
        return count


if __name__ == '__main__':
    day1 = Day1('inputs/task1.txt')
    print(day1.data)
    print(day1.part_1())
    print(day1.part_2())
