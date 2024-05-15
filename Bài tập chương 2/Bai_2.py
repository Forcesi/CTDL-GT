def Tam_Giac_Tren(mang):
    # Kiểm tra mang có phải ma trận vuông không
    n = len(mang)
    for hang in mang:
        if len(hang) != n:
            return False

    # Kiểm tra tính tam giác trên
    for i in range(n):
        for j in range( i + 1, n):
            if mang[i][j] != 0:
                return False
    return True

mang1 = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]

mang2 = [[1, 0, 3],
         [9, 2, 1],
         [6, 0, 6]]

print(Tam_Giac_Tren(mang1))  
print(Tam_Giac_Tren(mang2))  