from input_reader import Reader


class Day2:

    def __init__(self, file: str):
        self.data = Reader.string(file)
        self.final_data = self.parse_data()

    def parse_data(self):
        return [(line.split()[0], int(line.split()[1])) for line in self.data]

    def part_1(self) -> int:
        x = y = 0
        for instruction, unit in self.final_data:
            if instruction == 'forward':
                x += unit
            elif instruction == 'up':
                y -= unit
            elif instruction == 'down':
                y += unit
        return x * y

    def part_2(self) -> int:
        x = y = aim = 0
        for instruction, unit in self.final_data:
            if instruction == 'forward':
                x += unit
                y += (aim * unit)
            elif instruction == 'up':
                aim -= unit
            elif instruction == 'down':
                aim += unit
        return x * y


if __name__ == '__main__':
    day2 = Day2('inputs/task2.txt')
    print(day2.data)
    print(day2.part_1())
    print(day2.part_2())
