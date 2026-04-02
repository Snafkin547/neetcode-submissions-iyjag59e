class DSU:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.size = [1] *(n + 1)

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        elif self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parents[pv] = self.parents[pu]
        else:
            self.size[pv] += self.size[pu]
            self.parents[pu] = self.parents[pv]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)
        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]
        return []