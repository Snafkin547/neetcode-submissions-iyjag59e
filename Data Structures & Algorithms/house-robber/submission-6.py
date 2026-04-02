class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0

        for num in nums:
            best = max(num + prev, curr)
            prev = curr
            curr = best
        return curr
        
