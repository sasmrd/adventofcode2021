from src.input_reader import InputReader


class Day8:

    def __init__(self, file):
        self.data = InputReader.input_reader_string(file)

    def part_1(self, input_file):
        index = 0
        acc = 0
        visited = [False] * len(self.data)
        while True:
            if index >= len(visited):
                return acc, True
            elif visited[index]:
                return acc, False
            else:
                visited[index] = True
                operation = input_file[index][:3]
                arg = int(input_file[index][4:])
                if operation == 'acc':
                    acc += arg
                    index += 1
                elif operation == 'jmp':
                    index += arg
                elif operation == 'nop':
                    index += 1

    def part_2(self):
        for index in range(len(self.data)):
            input_file = self.data.copy()
            replace_dict = {'nop': 'jmp', 'jmp': 'nop'}
            for key in replace_dict.keys():
                if key in self.data[index]:
                    input_file[index] = input_file[index].replace(key, str(replace_dict[key]))
                    acc, successful = self.part_1(input_file)
                    if successful:
                        return acc, index


if __name__ == '__main__':
    day8 = Day8('inputs/task8.txt')
    print(day8.part_1(day8.data)[0])
    print(day8.part_2()[0])
