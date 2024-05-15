class Node:
    def __init__(self, he_so, so_mu):
        self.he_so = he_so
        self.so_mu = so_mu
        self.ke_tiep = None

class DaThuc:
    def __init__(self):
        self.head = None

    def them_so_hang(self, he_so, so_mu):
        new_node = Node(he_so, so_mu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.ke_tiep is not None:
                current = current.ke_tiep
            current.ke_tiep = new_node

    def DoiDau(self):
        current = self.head
        while current is not None:
            current.he_so = -current.he_so
            current = current.ke_tiep

# Sử dụng
da_thuc = DaThuc()
da_thuc.them_so_hang(10, 2)
da_thuc.them_so_hang(-2, 1)
da_thuc.them_so_hang(5, 0)

print("Đa thức ban đầu:")
current = da_thuc.head
while current is not None:
    print(f"{current.he_so}x^{current.so_mu}", end=" ")
    current = current.ke_tiep

da_thuc.DoiDau()

print("\n\nĐa thức sau khi đổi dấu:")
current = da_thuc.head
while current is not None:
    print(f"{current.he_so}x^{current.so_mu}", end=" ")
    current = current.ke_tiep