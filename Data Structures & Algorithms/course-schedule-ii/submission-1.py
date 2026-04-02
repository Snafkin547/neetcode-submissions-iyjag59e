class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        pre = {c: [] for c in range(n)}
        for c, p in prerequisites:
            pre[c].append(p)
        
        # cycle: A temp set for the current path
        # visited: A universal set to keep track of cleared node
        cycle, visited = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for p in pre[crs]:
                if dfs(p) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(n):
            if dfs(i) == False:
                return []
        return res
        
        