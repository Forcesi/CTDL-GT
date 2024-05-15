class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class DanhSachLienKet:
    def __init__(self):
        self.head = None

    def them_phan_tu(self, info):
        new_node = Node(info)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def DaoNguoc(self):
        stack = []
        current = self.head
        while current is not None:
            stack.append(current)
            current = current.next
        self.head = None
        while stack:
            node = stack.pop(0)
            node.next = self.head
            self.head = node

    def in_danh_sach(self):
        current = self.head
        while current is not None:
            print(current.info, end=" ")
            current = current.next
        print()

# Sử dụng
dslk = DanhSachLienKet()
dslk.them_phan_tu(3)
dslk.them_phan_tu(5)
dslk.them_phan_tu(7)
dslk.them_phan_tu(9)

print("Danh sách liên kết ban đầu:")
dslk.in_danh_sach()

dslk.DaoNguoc()

print("Danh sách liên kết sau khi đảo ngược:")
dslk.in_danh_sach()