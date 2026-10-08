class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value = 0
        for i, k in enumerate(prices): 
            if i + 1 < len(prices) and prices[i+1] > k: 
                value += (prices[i+1] - k)
        return value
        
        