class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        minV = prices[0]
        res = 0
        for p in prices:
            res = max(res, p - minV)
            minV = min(minV, p)
        return res

