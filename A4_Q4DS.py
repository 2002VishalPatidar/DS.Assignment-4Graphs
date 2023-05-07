from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def count_trees(self):
        visited = set()
        count = 0

        for v in range(self.vertices):
            if v not in visited:
                self.dfs(v, visited)
                count += 1

        return count

    def dfs(self, v, visited):
        visited.add(v)

        for neighbor in self.adj_list[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
# Create a forest with 5 trees
g = Graph(10)
g.add_edge(0, 1)
g.add_edge(2, 3)
g.add_edge(4, 5)
g.add_edge(6, 7)
g.add_edge(8, 9)

# Count the number of trees in the forest
print(g.count_trees())