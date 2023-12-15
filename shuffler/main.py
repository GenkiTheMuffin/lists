import random
list = []
for i in range (10):
    list.append(random.randrange(10))


def shuffler(lil_list):
    for i in range(10000000):
        randindex1 = random.randrange(0,len(lil_list))
        randindex2 = random.randrange(0,len(lil_list))
        temp = lil_list[randindex2]
        lil_list[randindex2] = lil_list[randindex1]
        lil_list[randindex1] = temp
        print(lil_list)


shuffler(list)