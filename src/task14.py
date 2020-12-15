import itertools
from src.input_reader import InputReader


class Day14:

    def __init__(self, file):
        self.data = InputReader.input_reader_string(file)

    def part_1(self):
        updated = {}
        for line in self.data:
            if "mask" in line:
                mask = self.split_after_equals(line)
                mask_dict = {}
                for i, character in enumerate(mask):
                    if character == "1" or character == "0":
                        mask_dict[i] = character

            elif "mem" in line:
                mem = int(line.split("[")[1].split("]")[0])
                value = int(self.split_after_equals(line))
                bin_value = self.get_36_bit_rep(value)

                for key, item in mask_dict.items():
                    bin_value[key] = item

                updated[mem] = self.get_int_value_of_36_bit_rep(bin_value)

        return self.get_total_of_values(updated)

    def part_2(self):
        updated = {}
        for line in self.data:
            if "mask" in line:
                mask = self.split_after_equals(line)
                mask_dict = {"0": [], "1": [], "X": []}
                for i, character in enumerate(mask):
                    mask_dict[character].append(i)

            elif "mem" in line:
                mem = int(line.split("[")[1].split("]")[0])
                value = int(self.split_after_equals(line))
                bin_mem = self.get_36_bit_rep(mem)

                for key, item in mask_dict.items():
                    if key == "1" or key == "X":
                        for index in item:
                            bin_mem[index] = key

                if "X" in bin_mem:
                    indices = [i for i, x in enumerate(bin_mem) if x == "X"]
                    bin_tuples = list(itertools.product(range(2), repeat=len(indices)))
                    for each in bin_tuples:
                        temp_bin_mem = bin_mem.copy()
                        for i in range(len(indices)):
                            temp_bin_mem[indices[i]] = str(each[i])
                        updated[self.get_int_value_of_36_bit_rep(temp_bin_mem)] = value

        return self.get_total_of_values(updated)

    @staticmethod
    def split_after_equals(inp):
        return inp.split(" = ")[1]

    @staticmethod
    def get_36_bit_rep(inp):
        return list("{:036b}".format(inp))

    @staticmethod
    def get_int_value_of_36_bit_rep(inp):
        return int("".join(inp), 2)

    @staticmethod
    def get_total_of_values(dictionary):
        total = 0
        for value in dictionary.values():
            total += value
        return total


if __name__ == '__main__':
    day14 = Day14('inputs/task14.txt')
    print("Part 1:", day14.part_1())
    print("Part 2:", day14.part_2())
