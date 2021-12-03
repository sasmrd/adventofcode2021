from input_reader import InputReader


class DayXYZ:

    def __init__(self, file):
        self.data = InputReader.input_reader_int(file)

    def part_1(self):
        print("part 1")
        return True

    def part_2(self):
        print("part 2")
        return True


if __name__ == '__main__':
    dayXYZ = DayXYZ('inputs/taskXYZ.txt')
    print(dayXYZ.data)
    print(dayXYZ.part_1())
    print(dayXYZ.part_2())
