class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                best_profit = max(best_profit, prices[j]-prices[i])
        return best_profit 
