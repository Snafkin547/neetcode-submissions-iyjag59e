class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        hold = float('-inf')
        sold = rest = 0
        for p in prices:
            prev = sold
            hold = max(hold, rest - p)
            sold = hold + p
            rest = max(rest, prev)
        return max(sold, rest)