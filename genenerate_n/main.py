import random

list = []


def generate_n(n: int):
    global list
    for i in range(n):
        list.append(random.randrange(5, 11))
    print(list)


generate_n(10)

list2 = []


def generate_n2(n: int):
    global list2
    for i in range(n):
        list2.append(i)
    print(list2)

generate_n2

