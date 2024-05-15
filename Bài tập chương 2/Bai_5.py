def Cong(a, b):
    # Tạo một danh sách rỗng để chứa kết quả
    ket_qua = []
    
    # Khởi tạo biến nhớ cho phần dư
    nho = 0
    
    # Xác định vị trí phần tử cuối cùng của mảng dài hơn
    max_len = max(len(a), len(b))
    
    # Duyệt qua các phần tử từ cuối lên đầu
    for i in range(max_len):
        # Lấy giá trị của các phần tử tương ứng trong a và b
        # Nếu vượt ra ngoài giới hạn của mảng, giá trị được coi là 0
        x = a[len(a) - i - 1] if i < len(a) else 0
        y = b[len(b) - i - 1] if i < len(b) else 0
        
        # Cộng hai phần tử tương ứng và phần dư
        tong = x + y + nho
        
        # Tính phần dư cho lần cộng tiếp theo
        nho = tong // 10
        
        # Thêm chữ số hàng đơn vị của tổng vào kết quả
        ket_qua.insert(0, tong % 10)
    
    # Nếu còn phần dư sau khi cộng hết các chữ số, thêm phần dư vào đầu kết quả
    if nho > 0:
        ket_qua.insert(0, nho)
    
    # Nếu kết quả có nhiều hơn 5 chữ số, thì coi như bị tràn số
    if len(ket_qua) > 5:
        return [-1]
    return ket_qua

a = [2, 2, 3, 3, 4]
b = [1, 2, 3, 4, 5]
print(Cong(a, b))  

c = [9, 2, 1, 2, 3]
d = [1, 8, 9, 8, 7]
print(Cong(c, d))  