class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(set)
        prereq_count = [0] * numCourses
        finished = 0

        # Build prereq count to keep track of how many prerequisites till completion
        for c, p in prerequisites: # Course, Prerequisite
            prereq_count[c] += 1
            prereq[p].add(c)
        
        # Complete no dependecies
        q = deque()
        for idx, task in enumerate(prereq_count):
            if task == 0:
                finished += 1
                q.append(idx)

        # See if I can complete all prerequisites without cycle
        while q:
            curr = q.popleft()
            for d in prereq[curr]: # Whats waiting for curr
                prereq_count[d] -= 1
                if not prereq_count[d]:
                    finished += 1
                    q.append(d)

        return finished  == numCourses
            
        '''
        When curr has prerequisites = > Work on it
        When prerequisites are all gone, unblock dependecies
        Detect cycle and immenent False
        Consider all done when no prerequs
        '''
        