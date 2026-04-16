class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.size[pu] > self.size[pv]:
                self.parent[pv] = pu
                self.size[pu] += self.size[pv]
            else:
                self.parent[pu] = pv
                self.size[pv] += self.size[pu]
            return True
        return False

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for a, b in edges:
            if dsu.union(a, b):
                res -= 1
        return res
                