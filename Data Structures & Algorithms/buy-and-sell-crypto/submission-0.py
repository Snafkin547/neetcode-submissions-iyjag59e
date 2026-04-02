class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        # buy, sell pointers
        buy, sell = 0, 1
        # Maintain profit
        profit = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]: # move buy to the lowest so far
                buy = sell
            else:
                profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        return profit
        