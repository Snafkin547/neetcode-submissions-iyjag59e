class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseD = defaultdict(list)
        
        for c, d in prerequisites:
            courseD[c].append(d)
        states = [0] * numCourses
        
        for i in range(numCourses):
            if states[i] == 0:

               stack = [(i, False)]
            
               while stack:
                    curr, processed = stack.pop()
                    if processed:
                       states[curr] = 2
                       continue
                    if states[curr] == 1: # already visiting
                       return False
                    if states[curr] == 2:
                       continue
                    states[curr]= 1
                    stack.append((curr, True))
            
                    for c in courseD[curr]:
                        stack.append((c, False))
        return True
