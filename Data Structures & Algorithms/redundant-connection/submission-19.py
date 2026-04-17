class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.size[pu] > self.size[pv]:
                self.parent[pv] = self.parent[pu]
                self.size[pu] += self.size[pv]
            else:            
                self.parent[pu] = self.parent[pv]
                self.size[pv] += self.size[pu]
            return False
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # If both belongs to same DSU
        n = len(edges)
        dsu = DSU(n)
        for a, b in edges:
            if dsu.union(a, b):
                res = [a, b]
        return res