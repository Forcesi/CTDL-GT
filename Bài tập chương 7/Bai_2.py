def SoThanhPhan(dt):
    # Khởi tạo một bộ đếm số thành phần liên thông
    so_thanh_phan = 0
    
    # Tạo một danh sách đánh dấu các đỉnh đã được duyệt
    danh_dau = [False] * len(dt)
    
    # Hàm duyệt đồ thị bằng thuật toán DFS
    def DFS(u):
        danh_dau[u] = True
        
        for v in dt[u]:
            if not danh_dau[v]:
                DFS(v)
    
    # Duyệt qua tất cả các đỉnh
    for u in range(len(dt)):
        if not danh_dau[u]:
            so_thanh_phan += 1
            DFS(u)
    
    # Trả về số thành phần liên thông
    return so_thanh_phan

# Đồ thị liên thông vô hướng
dt1 = {0: [1, 3], 1: [0, 2, 3], 2: [1, 3], 3: [0, 1, 2]}
print(SoThanhPhan(dt1))  # Output: 1

# Đồ thị không liên thông vô hướng
dt2 = {0: [1], 1: [0], 2: [3], 3: [2]}
print(SoThanhPhan(dt2))  # Output: 2

# Đồ thị liên thông hữu hướng
dt3 = {0: [1, 3], 1: [2], 2: [3], 3: []}
print(SoThanhPhan(dt3))  # Output: 1

# Đồ thị không liên thông hữu hướng
dt4 = {0: [1], 1: [], 2: [3], 3: []}
print(SoThanhPhan(dt4))  # Output: 2