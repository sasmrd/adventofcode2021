from input_reader import InputReader


class Day3:

    def __init__(self, file):
        self.data = InputReader.input_reader_string(file)
        self.dictionary = {k: [0, 0] for k in range(0, 12)}

    def part_1(self):
        for item in self.data:
            for i, char in enumerate(item):
                self.dictionary[i][int(char)] += 1
        gamma = ''
        epsilon = ''
        for v in self.dictionary.values():
            gamma += '0' if v[0] > v[1] else '1'
            epsilon += '1' if v[0] > v[1] else '0'
        bin_gamma = int(gamma, 2)
        bin_epsilon = int(epsilon, 2)
        return bin_epsilon * bin_gamma

    def part_2(self):
        oxygen_list = self.data
        for char_i in range(0, 12):
            temp_dict = {'0': [], '1': []}
            for i, number in enumerate(oxygen_list):
                if number[char_i] == '0':
                    temp_dict['0'].append(i)
                else:
                    temp_dict['1'].append(i)
            maximum = '1' if len(temp_dict['0']) <= len(temp_dict['1']) else '0'
            oxygen_list = [item for j, item in enumerate(oxygen_list) if j not in temp_dict[maximum]]
            if len(oxygen_list) == 1:
                break
        bin_oxygen = int(oxygen_list[0], 2)

        co2_list = self.data
        for char_i in range(0, 12):
            temp_dict = {'0': [], '1': []}
            for i, number in enumerate(co2_list):
                if number[char_i] == '0':
                    temp_dict['0'].append(i)
                else:
                    temp_dict['1'].append(i)
            print(temp_dict)
            minimum = '0' if len(temp_dict['0']) <= len(temp_dict['1']) else '1'
            co2_list = [item for j, item in enumerate(co2_list) if j not in temp_dict[minimum]]
            if len(co2_list) == 1:
                break
        bin_co2 = int(co2_list[0], 2)
        return bin_oxygen * bin_co2


if __name__ == '__main__':
    day3 = Day3('inputs/task3.txt')
    # print(day3.data)
    print(day3.part_1())
    print(day3.part_2())
