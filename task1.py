import itertools

f = open("task1.txt","r")

def find_pairs(lst, key):
    return [(a, b) for a, b in itertools.permutations(lst, 2) if a+b == key]


def find_triples(lst, key):
    return [(a, b, c) for a, b, c in itertools.permutations(lst, 3) if a+b+c == key]


def main():
    lst = []
    for num in f:
        lst.append(int(num))

    print(find_pairs(lst,2020)[0][0]*find_pairs(lst,2020)[0][1])
    
    print((find_triples(lst,2020)[0][0]*find_triples(lst,2020)[0][1]*find_triples(lst,2020)[0][2]))

main()