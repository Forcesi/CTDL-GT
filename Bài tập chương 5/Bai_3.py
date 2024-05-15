class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SonutLa(self, node):
        if node is None:
            return 0
        elif node.right is None and node.left is None :
            return 1
        else:
            return self.SonutLa(node.right) + self.SonutLa(node.left)

# Tạo một cây nhị phân để test
cay = BinaryTree()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)
cay.root.right.left = Node(6)
cay.root.right.right = Node(7)

# Gọi phương thức SonutLa() và in kết quả
print("Số nút lá của cây là:", cay.SonutLa(cay.root))        
