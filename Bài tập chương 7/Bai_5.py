from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BacDinh(self, v):
        if v not in self.graph:
            return 0
        return len(self.graph[v])

# Ví dụ sử dụng
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Bậc của đỉnh 0:", g.BacDinh(0))  # Output: 2
print("Bậc của đỉnh 1:", g.BacDinh(1))  # Output: 2
print("Bậc của đỉnh 2:", g.BacDinh(2))  # Output: 3
print("Bậc của đỉnh 3:", g.BacDinh(3))  # Output: 2
print("Bậc của đỉnh 4:", g.BacDinh(4))  # Output: 1
print("Bậc của đỉnh 5:", g.BacDinh(5))  # Output: 0