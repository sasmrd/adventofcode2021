from input_reader import Reader


class Day7:

    def __init__(self, file: str):
        self.data = Reader.one_line_int_list(file)

    def part_1(self) -> int:
        return min(
            sum(abs(fish - value) for fish in self.data)
            for value in range(0, max(self.data)))

    def part_2(self) -> int:
        return min(
            sum(0.5*abs(fish - value)*(abs(fish - value)+1) for fish in self.data)
            for value in range(0, max(self.data)))


if __name__ == '__main__':
    day7 = Day7('inputs/task7.txt')
    print(day7.data)
    print(day7.part_1())
    print(day7.part_2())
