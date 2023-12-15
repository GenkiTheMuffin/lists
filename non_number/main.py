list = [1, "kill", 2, ["i hate u"], "man", 56, "im dead"]


def non_num(list):
    result = []
    for i in list:
        if not isinstance(i, int):
            result.append(i)
    return result


print(non_num(list))
