class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DSU
        # count nodes
        # iterate over edges, save the latest cycle
        nodes = set()
        for a, b in edges:
            nodes.add(a)
            nodes.add(b)
        parent = list(range(len(nodes)+1))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(a, b):
            ua, ub = find(a), find(b)
            if ua == ub:
                return True
            parent[ub] = ua
            return False
        res = []
        for a, b in edges:
            if union(a, b):
                res = [a, b]
        return res
            