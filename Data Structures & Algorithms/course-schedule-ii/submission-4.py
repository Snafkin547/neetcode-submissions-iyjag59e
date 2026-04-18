class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        count = defaultdict(int)
        for a, b in prerequisites:
            mp[b].append(a)
            count[a] += 1
        res = []
        q = deque()
        for i in range(numCourses):
            if count[i] == 0:
                q.append(i)
        while q:
            c = q.popleft()
            res.append(c)
            for nei in mp[c]:
                count[nei] -= 1
                if count[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []
        