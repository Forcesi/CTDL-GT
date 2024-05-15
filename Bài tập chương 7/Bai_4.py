from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def ChuaDinh(self, v):
        return v in self.graph

# Ví dụ sử dụng
# Đồ thị vô hướng
g1 = Graph(directed=False)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
print("Đỉnh 0 là đỉnh của đồ thị:", g1.ChuaDinh(0))  # True
print("Đỉnh 3 là đỉnh của đồ thị:", g1.ChuaDinh(3))  # True
print("Đỉnh 4 là đỉnh của đồ thị:", g1.ChuaDinh(4))  # False

# Đồ thị có hướng
g2 = Graph(directed=True)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
print("Đỉnh 0 là đỉnh của đồ thị:", g2.ChuaDinh(0))  # True
print("Đỉnh 3 là đỉnh của đồ thị:", g2.ChuaDinh(3))  # False
print("Đỉnh 4 là đỉnh của đồ thị:", g2.ChuaDinh(4))  # False
