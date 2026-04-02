class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        cur = 0
        l, r = 0, 1
        buy = prices[l]
        
        while r < len(prices):
            cur = max(prices[r] - prices[l], cur)
            if prices[l] > prices[r]:
                l = r
            r += 1
        return cur
      