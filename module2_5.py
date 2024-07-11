def get_martrix(n, m, value):
    matrix = []

    for i in range(n):
        empty=[]
        matrix.append(empty)
        for j in range(m):
            empty.append(value)
    return matrix


result1 = get_martrix(2, 2, 10)
result2 = get_martrix(3, 5, 42)
result3 = get_martrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
