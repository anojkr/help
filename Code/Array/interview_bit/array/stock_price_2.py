class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        prices = A
        max_profit = 0
        l = len(prices)
        if l == 0 or l == 1:
            return 0
        
        for x in range(1, l):
            p = prices[x] - prices[x-1]
            if (p > 0):
                max_profit = max_profit + p
                
        return max_profit
            
