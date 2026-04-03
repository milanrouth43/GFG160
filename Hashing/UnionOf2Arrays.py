def findUnion(a, b):
    res = []
    for i in range(len(a)):
        j = 0
        while j < len(res):
            if res[j] == a[i]:
                break
            j += 1
        if j == len(res):
            res.append(a[i])
    for i in range(len(b)):
        j = 0
        while j < len(res):
            if res[j] == b[i]:
                break
            j += 1
        if j == len(res):
            res.append(b[i])

    return res


if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    res = findUnion(a, b)

    for value in res:
        print(value, end=" ")