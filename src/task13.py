import math
import numpy
from src.input_reader import InputReader


class Day13:

    def __init__(self, file):
        self.data = InputReader.input_reader_string(file)
        self.timestamp = int(self.data[0])
        self.buses = self.get_useful_input()
        self.bus_with_x = self.get_bus_x()

    def part_1(self):
        modulus = []
        for bus in self.buses:
            modulus.append(abs((self.timestamp % bus) - bus))
        minimum = min(modulus)
        minimum_bus = self.buses[modulus.index(minimum)]
        return minimum * minimum_bus

    def part_2(self):
        moduli_arg = {}
        for index, bus in enumerate(self.bus_with_x):
            if bus != 0:
                moduli_arg[bus] = ((-index) % bus)

        M = math.prod(moduli_arg.keys())
        a_ = list(moduli_arg.values())
        m_ = list(moduli_arg.keys())
        b_ = []
        for m in m_:
            b_.append(int(M/m))
        b_dash = []
        for i, b_i in enumerate(b_):
            b_dash.append(self.get_b_i_dash(b_i, m_[i]))

        x = 0
        for i in range(len(a_)):
            x += (a_[i]*b_[i]*b_dash[i])

        result = x
        while result > 0:
            result -= M
        result += M
        return result

    def get_useful_input(self):
        bus_string = self.data[1].replace("x,", "")
        bus_lst = bus_string.split(",")
        return [int(x) for x in bus_lst]

    def get_bus_x(self):
        bus_string = self.data[1].replace("x", "0")
        bus_lst = bus_string.split(",")
        return [int(x) for x in bus_lst]

    @staticmethod
    def get_b_i_dash(b_i, m_i):
        i = 1
        while i <= 100000:
            ans = ((b_i * i) - 1) % m_i
            if ans == 0:
                return i
            i += 1


if __name__ == '__main__':
    day13 = Day13('inputs/task13.txt')
    print("Part 1:", day13.part_1())
    print("Part 2:", day13.part_2())
