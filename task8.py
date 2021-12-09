import re

from input_reader import Reader


class Day8:

    def __init__(self, file: str):
        self.data = [x.split() for x in Reader.string(file)]
        self.outputs = [x[-4:] for x in self.data]

    def part_1(self) -> int:
        return sum(1 if len(line[i]) in [2, 3, 4, 7] else 0 for line in self.outputs for i in range(len(line)))

    def part_2(self) -> int:
        fixed_nums = {2: 1, 3: 7, 4: 4, 7: 8}  # len: number
        total = 0

        for line in self.data:
            nums = {i: 'x' for i in range(10)}

            signals = [''.join(sorted(x)) for x in line[:10]]
            output = [''.join(sorted(y)) for y in line[-4:]]

            nums.update({fixed_nums[len(s)]: s for s in signals if len(s) in fixed_nums.keys()})

            fives = [x for x in signals if len(x) == 5]
            sixes = [y for y in signals if len(y) == 6]

            # calculate 3
            nums[3] = list(filter(lambda num: set(nums[7]).issubset(set(num)), fives))[0]
            fives.remove(nums[3])

            # calculate 9
            nums[9] = list(filter(lambda num: set(nums[4]).issubset(set(num)), sixes))[0]
            sixes.remove(nums[9])

            # calculate 5
            nums[5] = list(filter(lambda num: (set(nums[4]) - set(nums[1])).issubset(set(num)), fives))[0]
            fives.remove(nums[5])

            # 2 is left over
            nums[2] = fives[0]

            # calculate 6
            nums[6] = list(filter(lambda num: set(nums[5]).issubset(set(num)), sixes))[0]
            sixes.remove(nums[6])

            # 0 is left over
            nums[0] = sixes[0]

            result = ''
            for char in output:
                result += str([k for k, v in nums.items() if char == v][0])
            total += int(result)

        return total


if __name__ == '__main__':
    day8 = Day8('inputs/task8.txt')
    print(day8.data)
    print(day8.part_1())
    print(day8.part_2())
