from src.input_reader import InputReader


class Day15:

    def __init__(self, file):
        self.data = InputReader.input_reader_one_line_int_list(file)

    def part_1(self):
        return self.get_result(2020)

    def part_2(self):
        return self.get_result(30000000)

    def get_result(self, position):
        inputs = self.data.copy()
        dictionary = {}
        for i, item in enumerate(inputs):
            dictionary[item] = [i]
        end = False
        while not end:
            lookup_value = inputs[-1]
            try:
                indices = dictionary[lookup_value]
            except KeyError:
                print(f"The key: '{lookup_value}' does not exist")
            else:
                if len(indices) == 1:
                    inputs.append(0)
                    dictionary[0].append(len(inputs)-1)
                elif len(indices) > 1:
                    num = indices[-1] - indices[-2]
                    inputs.append(num)
                    try:
                        dictionary[num].append(len(inputs)-1)
                    except KeyError:
                        dictionary[num] = [len(inputs) - 1]
            if len(inputs) == position:
                end = True
        return inputs[-1]


if __name__ == '__main__':
    day15 = Day15('inputs/task15.txt')
    print("Part 1:", day15.part_1())
    print("Part 2:", day15.part_2())
