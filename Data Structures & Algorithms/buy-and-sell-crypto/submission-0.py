class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            trans = prices[j] - prices[i]
            if trans > 0:
                profit = max(profit, trans)
            else:
                i = j
            j+=1

        return profit