from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.outbound = []
        self.inbound = []
    
    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)
    
    def __str__(self):
        return f'Node({self.value})'
    
class Graph:
    def __init__(self, root):
        self._root = root
    
    def dfs(self, current=None, visited=list()):
        if current is None:
            current = self._root
        visited.append(current)
        for next in current.outbound:
            if next not in visited:
                self.dfs(next, visited)
        return visited
    
    def bfs(self):
        visited = list()
        queue = deque()
        queue.append(self._root)
        visited.append(self._root)
        while queue:
            vertex = queue.popleft()
            for next in vertex.outbound:
                if next not in visited:
                    queue.append(next)
                    visited.append(next)
        return visited


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

g = Graph(a)
print(" ".join(map(str, g.bfs())))