class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        pre = {c: [] for c in range(n)}
        for c, p in prerequisites:
            pre[c].append(p)
        
        res = []
        s = []
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                s.append((i, False))
                while s:
                    crs, processed = s.pop()
                    if processed:
                        visited[crs] = 2
                        res.append(crs)
                        continue
                    if visited[crs] == 1:
                        return []
                    if visited[crs] == 2:
                        continue
                    visited[crs] = 1
                    s.append((crs, True))
                    for p in pre[crs]:
                        s.append((p, False))

        return res
            
            