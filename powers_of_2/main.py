def powers_of_2(n:int):
    result = [ ]
    for i in range(n):
        result.append(2**i)
    return result
print(powers_of_2(6))
