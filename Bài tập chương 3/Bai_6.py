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

    def Chep(self):
        new_dathuc = DaThuc()
        current = self.head
        while current is not None:
            new_dathuc.them_so_hang(current.he_so, current.so_mu)
            current = current.ke_tiep
        return new_dathuc

# Sử dụng
dathuc = DaThuc()
dathuc.them_so_hang(10, 2)
dathuc.them_so_hang(3, 1)
dathuc.them_so_hang(1, 0)

dathuc_copy = dathuc.Chep()

print("Đa thức ban đầu:")
current = dathuc.head
while current is not None:
    print(f"{current.he_so}x^{current.so_mu}", end=" ")
    current = current.ke_tiep

print("\n\nĐa thức sao chép:")
current = dathuc_copy.head
while current is not None:
    print(f"{current.he_so}x^{current.so_mu}", end=" ")
    current = current.ke_tiep