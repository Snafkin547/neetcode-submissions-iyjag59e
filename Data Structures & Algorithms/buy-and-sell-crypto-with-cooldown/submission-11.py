class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = sell = 0
        
        for i in range(n - 1, -1, -1):
            temp = buy1
            # Selling
            sell = max(sell, buy2 + prices[i])
            
            # Buying
            buy1 = max(buy1, sell - prices[i])
            buy2 = temp

        return buy1
