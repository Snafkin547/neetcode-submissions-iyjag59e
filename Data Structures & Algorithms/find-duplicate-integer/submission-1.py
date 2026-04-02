class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        holder = 0
        # bit operation
        for n in nums:
            if holder&(1<<n) !=0:
                return n
            holder ^= (1<<n)
        
                