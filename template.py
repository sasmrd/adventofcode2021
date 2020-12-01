def func(lst):
    pass


def main():
    f = open("task.txt","r")
    my_list = []
    for num in f:
        my_list.append(int(num))
    func(my_list)


main()
