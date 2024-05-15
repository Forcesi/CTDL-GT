class TuDien:
    def __init__(self):
        self.tu_dien = {} # Khởi tạo từ điển 

    # Hàm nhập từ, từ trái nghĩa và từ đồng nghĩa vào từ điển:
    def Nhaptu(self, tu, tu_dong_nghia = None, tu_trai_nghia = None):
        # Lấy ký tự đầu tiên của từ làm khoá:
        key = tu[0].upper()
        if key in self.tu_dien:
        # Nếu có, cập nhật giá trị cho khóa hiện có
            self.tu_dien[key][tu] = (tu_dong_nghia, tu_trai_nghia)
        else:
        # Nếu chưa có, thêm khóa mới vào từ điển
            self.tu_dien[key] = {tu: (tu_dong_nghia, tu_trai_nghia)}

    # Hàm tra cứu từ đồng nghĩa và trái nghĩa của từ trong từ điển:
    def Tratu(self, tu):
        # Lấy ký tự đầu tiên của từ làm khoá:
        key = tu[0].upper()
        if key in self.tu_dien:
        # Nếu có, tra cứu giá trị tương ứng với khóa
            if tu in self.tu_dien[key]:
                return self.tu_dien[key][tu]
            else:
                return None, None
        else:
            return None, None

# Ví dụ sử dụng
tu_dien = TuDien()

tu_dien.Nhaptu("defense", "protection", "offense")
tu_dien.Nhaptu("confident", "convinced", "unconfident")

word = input('Tra từ: ')

tu_dong_nghia, tu_trai_nghia = tu_dien.Tratu(word)
print(f"Từ đồng nghĩa của {word}: {tu_dong_nghia}")
print(f"Từ trái nghĩa của {word}: {tu_trai_nghia}")




