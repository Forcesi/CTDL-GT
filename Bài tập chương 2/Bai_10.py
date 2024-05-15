def Nhom_Cot(mang):
    n = len(mang) 
    
    # Tạo dictionary lưu trữ các nhóm cột giống nhau
    nhom_cot = {}

    # Duyệt qua các cột và tìm nhóm cho mỗi cột
    for i in range(n):
        cot = tuple(row[i] for row in mang)  # Lấy các phần tử của cột thứ i
        if cot in nhom_cot:
            nhom_cot[cot].append(i)
        else:
            nhom_cot[cot] = [i]

    # In ra các nhóm cột
    for nhom in nhom_cot.values():
        print(nhom)

mang1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mang2 = [[1, 2, 3], [6, 5, 4], [1, 2, 3]]

print("Nhóm cột của mang1:")
Nhom_Cot(mang1)
#[0]
#[1]
#[2]

print("\nNhóm cột của mang2:")
Nhom_Cot(mang2)
#[0] [2]
#[1]