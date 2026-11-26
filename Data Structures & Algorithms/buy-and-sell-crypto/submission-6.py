class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find best interval
        # update so-far best
        # when to move r and l if r < l
        
        res = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return res
