class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            ui, uj = find(i), find(j)
            if ui == uj:
                return False
            parent[uj] = ui
            return True

        cnt = n
        for u, v in edges:
            if union(u, v):
                cnt -= 1
        return cnt

                