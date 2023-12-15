sequence = [1, 5, 7, 12]
sequence2 = [4, 1, 5, 2, 7, 12]


def is_sorted(lil_list):
    for i in range(len(lil_list)):
        if lil_list[i + 1] >= lil_list[i]:
            return True
        else:
            return False


print(is_sorted(sequence))
print(is_sorted(sequence2))
