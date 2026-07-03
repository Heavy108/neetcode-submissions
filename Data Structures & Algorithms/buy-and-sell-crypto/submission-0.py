class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for l in range(0,len(prices)):
            for r in range(l+1 ,len(prices)):
                diff = prices[r] -prices[l]
                max_profit = max(max_profit,diff)
        return max_profit

        