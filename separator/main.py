import random

list = []


def generate_n(n: int):
    global list
    for i in range(n):
        list.append(random.randrange(0, 69))
    return list


def separator(lil_list):
    evens = []
    odds = []

    for i in lil_list:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return evens, odds


print(separator(generate_n(20)))

print(separator([2, 3, 5, 2, 1, 4, 6, 5, 3, 7])
