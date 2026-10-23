class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max1 = 0
        for i in range(n-1):
            for j in range(i,n):
                profit = prices[j] - prices[i]
                if profit > max1:
                    max1 = profit
        return max1            
        