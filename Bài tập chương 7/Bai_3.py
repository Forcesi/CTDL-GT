from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def ChuTrinh(self):
        visited = set()
        parent = {}

        for node in self.graph:
            if node not in visited:
                if self.bfs(node, visited, parent):
                    return True

        return False

    def bfs(self, start, visited, parent):
        queue = [start]
        visited.add(start)
        parent[start] = None

        while queue:
            node = queue.pop(0)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
                else:
                    if parent[node] != neighbor:
                        return True

        return False

# Ví dụ sử dụng
# Đồ thị vô hướng có chu trình
g1 = Graph(directed=False)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 4)
g1.add_edge(4, 1)
print("Đồ thị vô hướng có chu trình:", g1.ChuTrinh())  # True

# Đồ thị vô hướng không có chu trình
g2 = Graph(directed=False)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
g2.add_edge(3, 4)
print("Đồ thị vô hướng không có chu trình:", g2.ChuTrinh())  # False

# Đồ thị có hướng có chu trình
g3 = Graph(directed=True)
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 3)
g3.add_edge(3, 1)
print("Đồ thị có hướng có chu trình:", g3.ChuTrinh())  # True

# Đồ thị có hướng không có chu trình
g4 = Graph(directed=False)
g4.add_edge(0, 1)
g4.add_edge(1, 2)
g4.add_edge(2, 3)
g4.add_edge(3, 4)
print("Đồ thị có hướng không có chu trình:", g4.ChuTrinh())  # False