class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)

    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1  # Cây không phải là AVL

    return max(left_height, right_height) + 1

def KiemTraAVL(root):
    return height(root) != -1

# Trường hợp 1: Cây AVL
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

print("True")
print("Cây là AVL:" if KiemTraAVL(root) else "Cây không phải là AVL")

# Trường hợp 2: Cây không phải AVL
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)  # Thêm nút này để làm mất cân bằng cây

print("\nFalse")
print("Cây là AVL:" if KiemTraAVL(root) else "Cây không phải là AVL")