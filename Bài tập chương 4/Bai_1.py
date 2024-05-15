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

    def InNguoc(self):
        print("In ngược danh sách liên kết bằng đệ quy:")
        self.InNguocDeQuy(self.head)
        print("\n\nIn ngược danh sách liên kết bằng stack:")
        self.InNguocStack()

    def InNguocDeQuy(self, node):
        if node is None:
            return
        self.InNguocDeQuy(node.next)
        print(node.info, end=" ")

    def InNguocStack(self):
        stack = []
        current = self.head
        while current is not None:
            stack.append(current.info)
            current = current.next
        while stack:
            print(stack.pop(), end=" ")

# Sử dụng
dslk = DanhSachLienKet()
dslk.them_phan_tu(3)
dslk.them_phan_tu(5)
dslk.them_phan_tu(7)
dslk.them_phan_tu(9)

dslk.InNguoc()