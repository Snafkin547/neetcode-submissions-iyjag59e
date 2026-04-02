class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # state: i, buying
        n = len(prices)
        square = cooldown = 0
        holding = - prices[0]

        for i in range(2, n + 1):
            temp = square
            holding = max(cooldown - prices[i - 1], holding)
            square = max(holding + prices[i - 1], square)
            cooldown = temp 
        return square
