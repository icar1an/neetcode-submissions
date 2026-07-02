class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        for idx, i in enumerate(prices):
            profit.append(max(prices[idx:])-i)
        return max(profit)


        