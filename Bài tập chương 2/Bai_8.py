def Tam_Giac_Duoi(mang):
    n = len(mang) 
    
    # Duyệt qua các phần tử trên đường chéo chính và phía trên đường chéo chính
    for i in range(n):
        for j in range(i):
            if mang[i][j] != 0:
                return False
    
    # Nếu tất cả các phần tử trên đường chéo chính và phía trên đường chéo chính đều bằng 0
    # thì ma trận là ma trận tam giác dưới
    return True

mang1 = [[1, 0, 0], [4, 5, 0], [6, 7, 8]]
mang2 = [[1, 2, 0], [0, 5, 6], [0, 0, 8]]

print(Tam_Giac_Duoi(mang1)) 
print(Tam_Giac_Duoi(mang2))  