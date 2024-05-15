class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def Chep(root):
    if root is None:
        return None

    # Tạo một nút mới với cùng thông tin
    new_node = Node(root.info)

    # Đệ quy sao chép cây con bên trái
    new_node.left = Chep(root.left)

    # Đệ quy sao chép cây con bên phải
    new_node.right = Chep(root.right)

    return new_node

# Ví dụ sử dụng
# Tạo cây ban đầu
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Sao chép cây
new_root = Chep(root)

# In giá trị các nút của cây mới
def inorder(node):
    if node:
        inorder(node.left)
        print(node.info, end=" ")
        inorder(node.right)

print("Cây ban đầu: ", end="")
inorder(root)
print("\nCây mới: ", end="")
inorder(new_root)