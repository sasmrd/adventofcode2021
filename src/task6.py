from src.input_reader import InputReader


class Day6:

    def __init__(self, file):
        self.data = InputReader.input_reader_string_blank_lines(file)

    def part_1(self):
        total = 0
        for group in self.data:
            num = self.get_unique_letters(group)
            total += num

        return total

    def part_2(self):
        total = 0
        for group in self.data:
            num = self.get_intersection_letters(group)
            total += num

        return total

    @staticmethod
    def get_unique_letters(lst):
        all_letters = ''.join(map(str, lst))
        return len(set(list(all_letters)))

    @staticmethod
    def get_intersection_letters(lst):
        all_lists = []
        for person in lst.split():
            all_lists.append(list(person))
        return len(set.intersection(*map(set, all_lists)))


if __name__ == '__main__':
    day6 = Day6('inputs/task6.txt')
    print(day6.part_1())
    print(day6.part_2())
