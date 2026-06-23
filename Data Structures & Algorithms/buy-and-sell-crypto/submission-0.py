class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i,val in enumerate(prices):
            for j,val2 in enumerate(prices[i+1:]):
                if (val2-val)>profit:
                    profit = val2-val
        return profit