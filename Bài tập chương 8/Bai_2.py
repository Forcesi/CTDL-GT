class TuDien:
    def __init__(self):
        self.tu_dien = {} # Khởi tạo từ điển

    # Hàm nhập từ, từ đồng nghĩa và trái nghĩa vào từ điển:
    def Nhaptu(self, tu, tu_dong_nghia = None, tu_trai_nghia = None):
        # Lấy ký tự đầu tiên của từ làm khoá:
        key = tu[0].upper()
        if key in self.tu_dien:
        # Nếu có, cập nhật giá trị cho khóa hiện có
            self.tu_dien[key][tu] = (tu_dong_nghia, tu_trai_nghia)
        else:
        # Nếu chưa có, thêm khóa mới vào từ điển
            self.tu_dien[key] = {tu: (tu_dong_nghia, tu_trai_nghia)}

          