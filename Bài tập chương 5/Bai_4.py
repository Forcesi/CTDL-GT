class Node:
    def __init__(self, info):
        self.info = info
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SonutTrungGian(self, none):
        if none is None:
            return 0
        count = 0
        if none.left:
            if none.left.left or none.left.right:
                count += self.SonutTrungGian(none.left)
            else:
                count += 1
        if none.right:
            if none.right.left or none.right.right:
                count += self.SonutTrungGian(none.right)
            else:
                count += 1
        return count

# Tạo một cây nhị phân để test
cay = BinaryTree()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)
cay.root.right.left = Node(6)

# Gọi phương thức SonutTrungGian() và in kết quả
print("Số nút trung gian của cây là:", cay.SonutTrungGian(cay.root))