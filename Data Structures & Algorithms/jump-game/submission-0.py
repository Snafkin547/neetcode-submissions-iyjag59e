class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for n in nums:
            if curr < 0:
                return False
            curr = max(n, curr)
            curr -= 1
        return True