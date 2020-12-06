from src.input_reader import InputReader


class Day5:

    def __init__(self, file):
        self.data = InputReader.input_reader_string(file)

    def part_1(self):
        ids = []
        for entry in self.data:
            row = self.sort_f_b(entry[:7])
            col = self.sort_l_r(entry[7:])
            unique_id = (row * 8) + col
            ids.append(unique_id)
        ids.sort()
        print(max(ids))
        return ids

    @staticmethod
    def part_2(list_ids):
        ref_list = list(range(min(list_ids), max(list_ids) + 1))
        return set(ref_list).difference(list_ids)

    def sort_f_b(self, value):
        row = list(range(128))
        for letter in value:
            if letter == "F":
                row = self.split_list(row, 0)
            elif letter == "B":
                row = self.split_list(row, 1)
        return row[0]

    def sort_l_r(self, value):
        col = list(range(8))
        for letter in value:
            if letter == "L":
                col = self.split_list(col, 0)
            elif letter == "R":
                col = self.split_list(col, 1)
        return col[0]

    @staticmethod
    def split_list(a_list, side):
        half = len(a_list) // 2
        # 0 is bottom
        if side == 0:
            return a_list[:half]
        # 1 is top
        elif side == 1:
            return a_list[half:]


if __name__ == '__main__':
    day5 = Day5('inputs/task5.txt')
    all_ids = day5.part_1()
    print(day5.part_2(all_ids))
