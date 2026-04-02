class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: i, buying
        n = len(prices)
        dp = {}
        def helper(i, buying):
            if i >= n:
                return 0
            if (i, buying) in dp:
                return dp[i, buying]
            hold = helper(i + 1, buying)
            if buying:
                dp[(i, buying)] = max(hold, helper(i + 2, not buying) + prices[i])
            else:
                dp[(i, buying)] = max(hold, helper(i + 1, not buying) - prices[i])
            return dp[(i, buying)]
        
        return helper(0, False)

