import math


def get_fuel(mass):
    result = math.floor(int(mass)/3) - 2
    if result <= 0:
        return 0
    else:
        return result


def main1():
    f = open("aoc2019/practice1.txt", "r")

    total = 0
    for mass in f:
        total += get_fuel(mass)
    print(total)


def main2():
    f = open("aoc2019/practice1.txt", "r")

    total = 0
    for mass in f:
        zero = False
        while not zero:
            fuel = get_fuel(mass)
            if fuel == 0:
                zero = True
            else:
                mass = fuel
            total += fuel
    
    print(total)

main1()
main2()