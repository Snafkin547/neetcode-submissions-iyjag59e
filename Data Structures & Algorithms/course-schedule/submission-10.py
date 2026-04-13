class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visiting = set()
        mp = defaultdict(list)
        for main, dep in prerequisites:
            mp[main].append(dep)

        def helper(curr):
            if curr not in mp:
                return True

            if curr in visiting:
                return False

            visiting.add(curr)
            for d in mp[curr]:
                if not helper(d):
                    return False
            visiting.discard(curr)
            return True

        for i in range(numCourses):
            if not helper(i):
                return False
        return True
            