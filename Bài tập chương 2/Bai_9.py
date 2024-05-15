from collections import Counter

def Trung_Cot(mang):
    n = len(mang) 
    
    # Tạo danh sách các cột từ ma trận
    cot_list = [list(col) for col in zip(*mang)]
    
    # Sử dụng Counter để đếm số lần xuất hiện của các cột
    cot_count = Counter(map(tuple, cot_list))
    
    # Kiểm tra xem có ít nhất một cột xuất hiện nhiều hơn một lần
    return any(count > 1 for count in cot_count.values())

mang5 = [
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 10],
    [20, 30, 40, 50, 60],
    [80, 90, 10, 20, 30],
    [40, 50, 60, 70, 80]
]

mang6 = [
    [1, 2, 3, 4, 1],
    [6, 7, 8, 9, 6],
    [2, 3, 4, 5, 2],
    [7, 8, 9, 1, 7],
    [3, 4, 5, 6, 3]
]

print(Trung_Cot(mang5)) 
print(Trung_Cot(mang6))  