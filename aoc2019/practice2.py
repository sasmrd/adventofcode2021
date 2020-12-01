import itertools


def do_one(index, intcode):
    lookup_index1 = intcode[index+1]
    lookup_index2 = intcode[index+2]
    lookup_index3 = intcode[index+3]
    addition = intcode[lookup_index1] + intcode[lookup_index2]
    intcode[lookup_index3] = addition


def do_two(index, intcode):
    lookup_index1 = intcode[index+1]
    lookup_index2 = intcode[index+2]
    lookup_index3 = intcode[index+3]
    mult = intcode[lookup_index1] * intcode[lookup_index2]
    intcode[lookup_index3] = mult

def part1(intcode):
    for index in range(0, len(intcode), 4):
        if intcode[index] == 99:
            break
        elif intcode[index] == 1:
            do_one(index, intcode)
        elif intcode[intcode] == 2:
            do_two(index, intcode)
        else:
            continue

def part2(intcode):
    for pair in itertools.permutations(range(100), 2):
        print(pair)
        if sum(pair) > 10:
            break

part2([0,0])