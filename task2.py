from input_reader import InputReader


class Day2:

    def __init__(self, file):
        self.data = InputReader.input_reader_string(file)
        self.final_data = self.parse_data()

    def parse_data(self):
        return [line.split() for line in self.data]

    def part_1(self):
        x, y = 0, 0
        for instruction in self.final_data:
            if instruction[0] == 'forward':
                x += int(instruction[1])
            elif instruction[0] == 'up':
                y -= int(instruction[1])
            elif instruction[0] == 'down':
                y += int(instruction[1])
        return x * y

    def part_2(self):
        x, y, aim = 0, 0, 0
        for instruction in self.final_data:
            if instruction[0] == 'forward':
                x += int(instruction[1])
                y += (aim * int(instruction[1]))
            elif instruction[0] == 'up':
                aim -= int(instruction[1])
            elif instruction[0] == 'down':
                aim += int(instruction[1])
        return x * y


if __name__ == '__main__':
    day2 = Day2('inputs/task2.txt')
    print(day2.data)
    print(day2.part_1())
    print(day2.part_2())
