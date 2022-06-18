class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = profit = 0
        for sell in range(1, len(prices)):
            while buy < sell and prices[sell] < prices[buy]:
                buy += 1
            profit = max(profit, prices[sell]-prices[buy])
        return profit