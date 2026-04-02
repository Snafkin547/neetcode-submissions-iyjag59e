class DSU:
    def __init__(self, n):
        self.parents =list(range(n))
        self.size = [1] * n
    
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, u, v):
        up, vp = self.find(u), self.find(v)
        if up == vp:
            return False
        elif self.size[up] >= self.size[vp]:
            self.size[up] += self.size[vp]
            self.parents[vp] = up
        else:
            self.size[vp] += self.size[up]
            self.parents[up] = vp
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a, b in edges:
            if dsu.union(a, b):
                n -= 1
        return n
