from collections import Counter

from input_reader import InputReader


class Day6:

    def __init__(self, file):
        self.data = InputReader.input_reader_one_line_int_list(file)

    def part_1(self):
        fish_list = self.data.copy()
        temp_list = []
        for i in range(1, 81):
            for fish in fish_list:
                if fish == 0:
                    temp_list.extend([6, 8])
                else:
                    temp_list.append(fish - 1)
            fish_list = temp_list
            temp_list = []
        return len(fish_list)

    def part_2(self):
        fish_dict = dict(Counter(self.data))
        for i in range(1, 257):
            temp_dict = {k-1: v for k, v in fish_dict.items()}
            if -1 in temp_dict.keys():
                new = temp_dict.pop(-1)
                temp_dict[6] = temp_dict.get(6, 0) + new
                temp_dict[8] = temp_dict.get(8, 0) + new
            fish_dict = temp_dict
        return sum(fish_dict.values())


if __name__ == '__main__':
    day6 = Day6('inputs/task6.txt')
    print(day6.data)
    print(day6.part_1())
    print(day6.part_2())
