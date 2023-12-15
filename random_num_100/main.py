import random
result = []
def random_20():
    for i in range (1,21):
        result.append(random.randint(1,100))
    return result

print(random_20())
