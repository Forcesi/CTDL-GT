class SoNguyen:
    def __init__(self, a):
        self.a = a

    def Nhan(self, b):
        a_str = ''.join(str(x) for x in self.a)
        b_str = ''.join(str(x) for x in b)
        result = int(a_str) * int(b_str)

        # Kiểm tra xem kết quả có vượt quá giới hạn của số nguyên 32 bit không
        if result > 2**31 - 1 or result < -2**31:
            return [-1]
        else:
            return result

a = SoNguyen([1, 2, 3])
print(a.Nhan([4, 5, 6])) 
