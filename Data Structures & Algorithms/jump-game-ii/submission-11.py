class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        start = end = 0
        # Find the next range to look up furthest
        while end < n -1:
            furthest = 0
            for i in range(start, end + 1):
                furthest = max(furthest, i + nums[i])
            start = end + 1 # Next iter starts from current end + 1
            end = furthest # The next exploration till currently reachable furthest
            res += 1
        return res