from typing import List

from input_reader import Reader


class Day4:

    def __init__(self, file: str):
        self.data = Reader.string_blank_lines(file)
        self.bingo_numbers = self.data[0].split(',')
        self.squares = [x.split() for x in self.data[1:]]

    @staticmethod
    def is_complete_square(square: List[str]) -> bool:
        if square.count('X') < 5:
            return False
        # check rows
        for i in range(0, 25, 5):
            if square[i:i+5].count('X') == 5:
                return True
        # check columns
        for i in range(0, 5):
            if [square[0+i], square[5+i], square[10+i], square[15+i], square[20+i]].count('X') == 5:
                return True
        return False

    def part_1(self) -> int:
        for number in self.bingo_numbers:
            for i, square in enumerate(self.squares):
                try:
                    index = square.index(number)
                    self.squares[i][index] = 'X'
                    if self.is_complete_square(square):
                        return int(number) * sum([int(x) for x in square if x != 'X'])
                except ValueError:
                    continue

    def part_2(self) -> int:
        my_dictionary = {}
        for i, square in enumerate(self.squares):
            for j, number in enumerate(self.bingo_numbers):
                try:
                    index = square.index(number)
                    self.squares[i][index] = 'X'
                    if self.is_complete_square(square):
                        my_dictionary[j] = (int(number), sum([int(x) for x in square if x != 'X']))
                        break
                except ValueError:
                    continue
        maximum = max(my_dictionary, key=int)
        return my_dictionary[maximum][0] * my_dictionary[maximum][1]


if __name__ == '__main__':
    day4 = Day4('inputs/task4.txt')
    print(day4.part_1())
    print(day4.part_2())
