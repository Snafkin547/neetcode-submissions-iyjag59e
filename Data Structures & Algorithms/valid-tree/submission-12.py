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
        if pu == pv:
            return True
        else:
            if self.size[pu] > self.size[pv]:
                self.size[pu] += self.size[pv]
                self.parent[pv] = pu
            else:
               self.size[pv] += self.size[pu]
               self.parent[pu] = pv
            return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)
        node = dsu.find(0)
        for i in range(n):
            if not dsu.union(node, i):
                return False
        return True
        