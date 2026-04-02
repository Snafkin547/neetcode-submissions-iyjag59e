class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
         courseD = defaultdict(list)
         dependecy = [0] * numCourses

         for c, pre in prerequisites:
            courseD[pre].append(c) # Blockers
            dependecy[c] += 1 # How many dependecy to clear before this
         
         q = deque()
         for i in range(numCourses):
            if not dependecy[i]:
               q.append(i)

         finished = 0
         while q:
            c = q.popleft()
            finished += 1
            for n in courseD[c]:
               dependecy[n] -=1
               # Queue up if no blockers
               if dependecy[n] == 0:
                  q.append(n)
         return numCourses == finished
