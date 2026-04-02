class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False

        parent = list(range(n))
        print(parent)
        
        def find(i):
            if parent[i]!=i:
                parent[i] = find(parent[i])
                return parent[i]
            else:
                return i
        
        def union(i, j):
            ui, uj = find(i), find(j)
            if ui == uj:
                return False
            parent[uj] = ui
            return True
        for i, j in edges:
            if not union(i, j):
                return False
        return True
