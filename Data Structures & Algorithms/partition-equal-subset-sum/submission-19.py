class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = sum(nums)
        if res != (res >> 1) << 1:
            return False
        res >>= 1
        dp = [False] * (res + 1)
        dp[0] = True
        for n in nums:
            for i in range(res, n - 1, -1):
                dp[i] = dp[i - n] | dp[i]
        return dp[res]     
'''
Version 1 (Forward Loop) — The "Unbounded" Error
In the first version, your inner loop moves forward: for i in range(n, res + 1):.

The Problem: When you move forward, you use the updated values from the current iteration. This means if you have a 2, the code checks if it can make 2, then uses that result to see if it can make 4, then 6, and so on.

Result: It acts as if you have an infinite supply of each number.

Example: If nums = [2, 10], the target is 6. Version 1 would say True because it uses the number 2 three times. The correct answer is False.
'''   