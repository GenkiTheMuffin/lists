list = [1, "kill", 2, ["i hate u"], "man", 56, "im dead"]


def join_list(list):
    result = ""
    for i in list:
        i = str(i)
        result += i

    return result


print(join_list(list))
