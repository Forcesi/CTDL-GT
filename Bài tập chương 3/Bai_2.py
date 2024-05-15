class DaThuc:
    def __init__(self):
        self.arr = []

    def Them(self, heso, somu):
        self.arr.append((heso, somu))

    def RutGon(self):
        # Sắp xếp mảng theo thứ tự giảm dần của số mũ
        self.arr.sort(key=lambda x: x[1], reverse=True)

        # Rút gọn đa thức
        i = 0
        while i < len(self.arr) - 1:
            if self.arr[i][1] == self.arr[i + 1][1]:
                self.arr[i] = (self.arr[i][0] + self.arr[i + 1][0], self.arr[i][1])
                self.arr.pop(i + 1)
            else:
                i += 1

        # Loại bỏ các số hạng có hệ số bằng 0
        self.arr = [x for x in self.arr if x[0] != 0]

    def InDaThuc(self):
        is_first = True
        for heso, somu in self.arr:
            if is_first:
                print(f"{heso}x^{somu}", end="")
                is_first = False
            else:
                print(f" + {heso}x^{somu}", end="")

# Tạo một đa thức
dathuc = DaThuc()
dathuc.Them(2, 3)  # 2x^3
dathuc.Them(-1, 2)  # -x^2
dathuc.Them(4, 1)  # 4x
dathuc.Them(3, 0)  # 3
dathuc.Them(1, 2)  # x^2
dathuc.Them(-2, 1)  # -2x

# In ra đa thức trước khi rút gọn
print("Đa thức trước khi rút gọn:")
dathuc.InDaThuc()
print()  # Để xuống dòng

# Rút gọn đa thức
dathuc.RutGon()

# In ra đa thức sau khi rút gọn
print("Đa thức sau khi rút gọn:")
dathuc.InDaThuc()
print()  # Để xuống dòng

