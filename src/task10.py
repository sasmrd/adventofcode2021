from src.input_reader import InputReader


class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = self.get_graph_dict()

    def get_graph_dict(self):
        graph_dict = {}
        for start, end in self.edges:
            if start in graph_dict:
                graph_dict[start].append(end)
            else:
                graph_dict[start] = [end]
        return graph_dict

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end , path)
                for p in new_paths:
                    paths.append(p)

        return paths




class Day10:

    def __init__(self, file):
        self.data = InputReader.input_reader_int(file)

    def part_1(self):
        input_list = self.get_input_list()
        one_jolt = 0
        three_jolt = 0
        for index, adapter in enumerate(input_list):
            try:
                # print(adapter, input_list[index + 1], "diff =", input_list[index + 1] - adapter)
                if input_list[index+1] - adapter == 1:
                    one_jolt += 1
                elif input_list[index+1] - adapter == 3:
                    three_jolt += 1
            except IndexError:
                return one_jolt * three_jolt

    def part_2(self):
        input_list = self.get_input_list()
        routes = self.get_routes(input_list)
        route_graph = Graph(routes)
        all_paths = route_graph.get_paths(min(input_list), max(input_list))
        # print(all_paths)
        return len(all_paths)

    def get_input_list(self):
        input_list = self.data.copy()
        input_list.sort(key=int)
        input_list.append(max(input_list)+3)
        print(input_list)
        return input_list

    @staticmethod
    def get_routes(input_list):
        routes = []
        for node in input_list:
            if (node+1) in input_list:
                routes.append((node, node+1))
            if (node+2) in input_list:
                routes.append((node, node + 2))
            if (node+3) in input_list:
                routes.append((node, node + 3))
        return routes


if __name__ == '__main__':
    day10 = Day10('inputs/task10t.txt')
    print("Part 1:", day10.part_1(), "\n")
    print("Part 2:", day10.part_2(), "\n")
