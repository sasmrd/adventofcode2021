import networkx as nx
from input_reader import InputReader


class Day10:

    def __init__(self, file):
        self.data = InputReader.input_reader_int(file)

    def part_1(self):
        input_list = self.get_input_list()
        one_jolt = 0
        three_jolt = 0
        for index, adapter in enumerate(input_list):
            try:
                if input_list[index+1] - adapter == 1:
                    one_jolt += 1
                elif input_list[index+1] - adapter == 3:
                    three_jolt += 1
            except IndexError:
                return one_jolt * three_jolt

    def part_2(self):
        input_list = self.get_input_list()
        routes, splits = self.get_routes(input_list)
        ranges = self.ranges(splits)

        prod = 1
        for each in ranges:
            g = nx.Graph()
            this_range = input_list[input_list.index(each[0]): input_list.index(each[1])+1]
            small_route = self.get_routes(this_range)[0]
            g.add_edges_from(small_route)
            paths = []
            for path in nx.all_simple_paths(g, source=each[0], target=each[1]):
                path.sort()
                paths.append(path)
            set_paths = set(tuple(row) for row in paths)

            prod *= len(set_paths)
        return prod

    def get_input_list(self):
        input_list = self.data.copy()
        input_list.sort(key=int)
        input_list.append(max(input_list)+3)
        return input_list

    @staticmethod
    def get_routes(input_list):
        routes = []
        splits = []
        for node in input_list:
            next_steps = [node]
            if (node+1) in input_list:
                routes.append((node, node+1))
                next_steps.append(node+1)
            if (node+2) in input_list:
                routes.append((node, node + 2))
                next_steps.append(node+2)
            if (node+3) in input_list:
                routes.append((node, node + 3))
                next_steps.append(node+3)
            if len(next_steps) > 2:
                splits.extend(next_steps)
        splits = list(dict.fromkeys(splits))
        return routes, splits

    @staticmethod
    def ranges(nums):
        nums = sorted(set(nums))
        gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s + 1 < e]
        edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
        return list(zip(edges, edges))


if __name__ == '__main__':
    day10 = Day10('inputs/task10.txt')
    print("Part 1:", day10.part_1())
    print("Part 2:", day10.part_2())
