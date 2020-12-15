class InputReader:

    @staticmethod
    def input_reader_string(file_name):
        with open(file_name, "r") as f:
            return [x.strip() for x in f.readlines()]

    @staticmethod
    def input_reader_int(file_name):
        with open(file_name, "r") as f:
            return [int(x.strip()) for x in f.readlines()]

    @staticmethod
    def input_reader_list(file_name):
        with open(file_name, "r") as f:
            return [list(x.strip()) for x in f.readlines()]

    @staticmethod
    def input_reader_one_line_int_list(file_name):
        with open(file_name, "r") as f:
            line = f.readline()
            lst = line.split(",")
            return [int(x) for x in lst]

    @staticmethod
    def input_reader_string_blank_lines(file_name):
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
