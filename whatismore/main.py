import random

list = []


def generate_n(n: int):
    global list
    for i in range(n):
        list.append(random.randrange(5, 11))
    print(list)


def whatismore(lil_list):
    sume = 0
    sumo = 0
    for i in lil_list:
        if i % 2 ==0:
            sume +=1
        else:
            sumo+=1
    if sume > sumo:
        return "even"
    else:
        return "odd"
    
generate_n(5)
    
print(whatismore(list))


