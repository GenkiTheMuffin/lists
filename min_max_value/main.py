import random

list = []


def generate_n(n: int):
    global list
    for i in range(n):
        list.append(random.randrange(5, 11))
    print(list)


def max_value(lil_list):
    temp = lil_list[0]
    temp_index = 0
    for i in range(1,len(lil_list)):
        if lil_list[i] > temp:
            temp = lil_list[i]
            temp_index = i
    return (temp, temp_index)

generate_n(15)
print(max_value(list))


def sum_equals(lil_list):
    result = 0
    for i in lil_list:
        if i % 2 == 0:
            result += i
    return result

print(sum_equals(list))


def sum_equals_index(lil_list):
    result = 0 
    for i in range(len(lil_list)):
            if i %2 == 0:
                result += i
    return result