class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2:
            return False
        dp = {}
        
        def helper(i, balance):
            if balance == 0:
                return True
            if i == n or balance <0:
                return False
            
            if (i, balance) in dp:
                return dp[(i, balance)]
            
            dp[(i, balance)] = helper(i + 1, balance - nums[i]) or helper(i + 1, balance)
            return dp[(i, balance)]
        return helper(0, total//2)