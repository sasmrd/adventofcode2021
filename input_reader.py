from typing import List


class Reader:

    @staticmethod
    def string(file_name: str) -> List[str]:
        with open(file_name, "r") as f:
            return [x.strip() for x in f.readlines()]

    @staticmethod
    def integer(file_name: str) -> List[int]:
        with open(file_name, "r") as f:
            return [int(x.strip()) for x in f.readlines()]

    @staticmethod
    def list(file_name: str) -> List[List]:
        with open(file_name, "r") as f:
            return [list(x.strip()) for x in f.readlines()]

    @staticmethod
    def one_line_int_list(file_name: str) -> List[int]:
        with open(file_name, "r") as f:
            line = f.readline()
            lst = line.split(",")
            return [int(x) for x in lst]

    @staticmethod
    def string_blank_lines(file_name: str) -> List[str]:
        with open(file_name, "r") as f:
            temp_list = [x.strip() for x in f.readlines()]
            current = []
            my_list = []
            for entry in temp_list:
                if entry == '':
                    my_list.append(' '.join(current))
                    current = []
                elif entry == '-':
                    break
                else:
                    current.append(entry)
            return my_list
