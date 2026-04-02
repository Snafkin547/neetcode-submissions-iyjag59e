class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseD = defaultdict(list)
        
        for c, d in prerequisites:
            courseD[c].append(d)

        for i in range(numCourses):
            q = deque(courseD[i])
            taking = set()
               
            while q:
                curr = q.popleft()
                if curr == i:
                   return False
                for c in courseD[curr]:
                   q.append(c)
            del courseD[i]
        return True
