class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]          # cheapest price so far
        best_profit = 0

        for price in prices:
            lowest = min(lowest, price)                      # cheapest day to have bought, up to today
            best_profit = max(best_profit, price - lowest)   # profit if you sell today
        return best_profit