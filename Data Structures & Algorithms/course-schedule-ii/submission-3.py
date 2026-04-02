class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # course, prerequisite
        ordering = []
        count_dependecy = [0] * numCourses
        prereq = defaultdict(set)
        for c, p in prerequisites:
            count_dependecy[c] += 1
            prereq[p].add(c)

        q = deque()
        for i in range(numCourses):
            if count_dependecy[i] == 0:
                ordering.append(i)
                q.append(i)
        # Unblock dependecies
        while q:
            curr = q.popleft()
            for c in prereq[curr]:
                count_dependecy[c] -= 1
                if count_dependecy[c] == 0:
                    ordering.append(c)
                    q.append(c)

        return ordering if len(ordering) == numCourses else []