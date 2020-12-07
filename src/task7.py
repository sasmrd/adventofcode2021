from src.input_reader import InputReader


class Day7:

    def __init__(self, file):
        self.data = InputReader.input_reader_string(file)

    def part_1(self):
        tree = {}
        for line in self.data:
            rule, values = self.get_tree_values(line)
            tree[rule] = values
        bags = []
        for rule in tree.items():
            if self.check_if_contains_type(rule[1], "shiny gold"):
                bags.append(rule[0])
        for bag in bags:
            for rule in tree.items():
                if self.check_if_contains_type(rule[1], bag):
                    bags.append(rule[0])
        return len(set(bags))

    def part_2(self):
        tree = {}
        for line in self.data:
            rule, values = self.get_tree_values(line)
            tree[rule] = values
        print(self.traverse_the_tree(tree, 'shiny gold'))

    @staticmethod
    def get_tree_values(entry):
        key = entry.split(' bags contain ')[0]
        remaining = entry.split(' bags contain ')[1].replace(".", "")
        values = remaining.replace(" bags", "").replace(" bag", "").split(', ')
        rule_dict = {}
        for value in values:
            if "no other" in value:
                rule_dict["no other"] = 0
            else:
                number = int(value.split(' ')[0])
                colour = value[len(str(number))+1:]
                rule_dict[colour] = number
        return key, rule_dict

    @staticmethod
    def check_if_contains_type(lst, bag_type: str) -> bool:
        for item in lst:
            if bag_type in item:
                return True
        return False

    def traverse_the_tree(self, tree, key) -> int:
        if key == "no other":
            return 0
        sum_for_key = 0
        for each in tree[key].values():
            sum_for_key += int(each)
        return sum_for_key + sum([tree[key][colour] * self.traverse_the_tree(tree, colour) for colour in tree[key]])


if __name__ == '__main__':
    day7 = Day7('inputs/task7.txt')
    print(day7.part_1())
    day7.part_2()
