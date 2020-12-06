from src.input_reader import InputReader


class Day2:

    def __init__(self, file):
        self.data = InputReader.input_reader_string(file)

    @staticmethod
    def get_all_items(entry):
        lower = int(entry.split('-')[0])
        right_section = entry.split('-')[1]
        upper = int(right_section.split(" ")[0])
        section_right = right_section.split(" ")[1]
        letter = section_right.split(":")[0]
        password = right_section.split(": ")[1]
        return lower, upper, letter, password

    def part_1(self, a_list) -> int:
        count = 0
        for line in a_list:
            lower, upper, letter, password = self.get_all_items(line)
            total = 0

            for character in password:
                if character == letter:
                    total += 1

            if lower <= total <= upper:
                count += 1

        return count

    def part_2(self, a_list) -> int:
        count = 0
        for line in a_list:
            left_index, right_index, letter, password = self.get_all_items(line)

            try:
                left = password[left_index - 1]
                right = password[right_index - 1]

            except IndexError:
                left = ""

            finally:
                if (left == letter) and (right != letter):
                    valid = True
                elif (left != letter) and (right == letter):
                    valid = True
                else:
                    valid = False

                if valid:
                    count += 1
                else:
                    count = count
        return count


if __name__ == '__main__':
    day2 = Day2('inputs/task2.txt')
    print(day2.part_1(day2.data))
    print(day2.part_2(day2.data))
