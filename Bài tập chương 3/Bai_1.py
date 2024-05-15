class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.ke_tiep = None

class DaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        # Tạo một nút mới cho số hạng mới
        new_node = Node(heso, somu)

        # Nếu danh sách liên kết rỗng
        if self.head is None:
            self.head = new_node
            return

        # Nếu số mũ của nút mới lớn hơn số mũ của nút đầu tiên
        if new_node.somu > self.head.somu:
            new_node.ke_tiep = self.head
            self.head = new_node
            return

        # Duyệt qua danh sách liên kết để tìm vị trí chèn
        current = self.head
        while current.ke_tiep is not None and current.ke_tiep.somu >= new_node.somu:
            current = current.ke_tiep

        # Chèn nút mới vào vị trí thích hợp
        new_node.ke_tiep = current.ke_tiep
        current.ke_tiep = new_node

# Tạo một đa thức rỗng
dathuc = DaThuc()

# Thêm các số hạng vào đa thức
dathuc.Them(2, 3)  # Thêm số hạng 2x^3
dathuc.Them(-1, 2)  # Thêm số hạng -x^2
dathuc.Them(4, 1)  # Thêm số hạng 4x
dathuc.Them(3, 0)  # Thêm số hạng 3

# Duyệt qua danh sách liên kết để in ra các số hạng
current = dathuc.head
is_first = True
while current is not None:
    if is_first:
        print(f"{current.heso}x^{current.somu}", end="")
        is_first = False
    else:
        print(f" + {current.heso}x^{current.somu}", end="")
    current = current.ke_tiep

# Kết quả: 2x^3 + -x^2 + 4x + 3