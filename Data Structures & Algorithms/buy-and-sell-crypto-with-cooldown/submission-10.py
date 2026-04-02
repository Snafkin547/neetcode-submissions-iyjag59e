class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        
        prev, hold, unhold = 0, -prices[0], 0
        
        for i in range(1, n):
            temp = unhold
            # Not holding
            unhold = max(unhold, hold + prices[i])
            
            # Holding
            hold = max(hold, prev - prices[i])
            prev = temp

        return unhold
