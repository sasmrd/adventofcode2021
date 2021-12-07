from input_reader import Reader


class DayXYZ:

    def __init__(self, file: str):
        self.data = Reader.integer(file)

    def part_1(self) -> int:
        return 1

    def part_2(self) -> int:
        return 2


if __name__ == '__main__':
    dayXYZ = DayXYZ('inputs/taskXYZ.txt')
    print(dayXYZ.data)
    print(dayXYZ.part_1())
    print(dayXYZ.part_2())
