class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deg = [0] * numCourses
        nei = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            nei[b].append(a)
            deg[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if deg[i] == 0:
                q.append(i)
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for n in nei[curr]:
                deg[n] -= 1
                if deg[n] == 0:
                    q.append(n)

        return res if numCourses == len(res) else []
            