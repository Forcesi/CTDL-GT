def Nhom_Hang(mang):
    n = len(mang)
    # Kiểm tra mang có phải ma trận vuông không
    for hang in mang:
        if len(hang) != n:
            return False
    
    # Lưu trữ các nhóm hàng giống nhau
    nhom_hang = []
    
    # Duyệt qua các hàng
    for i in range(n):
        hang_i = mang[i]
        nhom_i = [i]  # Khởi tạo nhóm với chỉ mục hàng hiện tại
        
        # Tìm các hàng giống với hàng hiện tại
        for j in range(i+1, n):
            if mang[j] == hang_i:
                nhom_i.append(j)
        
        # Nếu nhóm chứa nhiều hơn một hàng, thêm vào danh sách nhóm hàng
        if len(nhom_i) > 1:
            nhom_hang.append(nhom_i)
    
    # In ra các nhóm hàng
    for nhom in nhom_hang:
        print("Nhóm hàng:", nhom)

mang = [[3, 5, 7],
        [2, 4, 6],
        [3, 5, 7]]

Nhom_Hang(mang)