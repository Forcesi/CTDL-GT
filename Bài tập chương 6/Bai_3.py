def Giao(a, b):
    array_1 = set(a)
    array_2 = set(b)

    array_3 = array_1 & array_2
    c = sorted(list(array_3))

    return c

# Ví dụ sữ dụng:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Giao(a, b)
print(c)