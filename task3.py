from input_reader import InputReader


class Day3:

    def __init__(self, file):
        self.data = InputReader.input_reader_string(file)
        self.dictionary = {k: [0, 0] for k in range(0, 12)}

    def part_1(self):
        for item in self.data:
            for i, char in enumerate(item):
                self.dictionary[i][int(char)] += 1
        gamma = epsilon = ''
        for v in self.dictionary.values():
            gamma += '0' if v[0] > v[1] else '1'
            epsilon += '1' if v[0] > v[1] else '0'
        return int(gamma, 2) * int(epsilon, 2)

    def part_2(self):
        oxygen_list = self.data.copy()
        for char_i in range(0, 12):
            temp_dict = {'0': [], '1': []}
            for i, number in enumerate(oxygen_list):
                temp_dict[number[char_i]].append(i)
            maximum = '1' if len(temp_dict['0']) <= len(temp_dict['1']) else '0'
            oxygen_list = [item for j, item in enumerate(oxygen_list) if j not in temp_dict[maximum]]
            if len(oxygen_list) == 1:
                break

        co2_list = self.data.copy()
        for char_i in range(0, 12):
            temp_dict = {'0': [], '1': []}
            for i, number in enumerate(co2_list):
                temp_dict[number[char_i]].append(i)
            minimum = '0' if len(temp_dict['0']) <= len(temp_dict['1']) else '1'
            co2_list = [item for j, item in enumerate(co2_list) if j not in temp_dict[minimum]]
            if len(co2_list) == 1:
                break
        return int(oxygen_list[0], 2) * int(co2_list[0], 2)


if __name__ == '__main__':
    day3 = Day3('inputs/task3.txt')
    print(day3.data)
    print(day3.part_1())
    print(day3.part_2())
