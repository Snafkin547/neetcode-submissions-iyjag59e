class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        curr = 0
        for idx, n in enumerate(nums):
            curr = max(curr, n)
            if idx != len(nums) -1 and not curr:
                return False
            curr -=1
            
        return True