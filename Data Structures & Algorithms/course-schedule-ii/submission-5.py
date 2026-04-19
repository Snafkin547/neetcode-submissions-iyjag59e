class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Keep adding non dependent 
        count = defaultdict(int)
        mp = defaultdict(list)
        for a, b in prerequisites:
            mp[b].append(a)
            count[a] += 1

        q = deque()
        for i in range(numCourses):
            if count[i] == 0:
                q.append(i)
        
        res = []
        while q:
            task = q.popleft()
            res.append(task)
            for nei in mp[task]:
                count[nei] -= 1
                if count[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []
                
            
            