class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Count how many prereq for each course
        # Complete zero dependencies and decrement courses that depend on them
        # Need counter/course and dependent map

        counter = [0] * numCourses
        dependent = defaultdict(list)

        for sec, prim in prerequisites:
            dependent[prim].append(sec)
            counter[sec] += 1
        
        q = deque()
        for i in range(numCourses):
            # Queue tasks w/o dependecy
            if counter[i] == 0:
                q.append(i)

        res = 0
        while q:
            # Execute tasks no dependecy and count completion
            curr = q.popleft()
            res += 1

            # Decrement course depending on curr course
            for d in dependent[curr]:
                counter[d] -= 1
                # If no more dependecies, put it on the queue
                if counter[d] == 0:
                    q.append(d)

        return res == numCourses # True only if all tasks have been executed