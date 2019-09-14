class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        
        n = len(A)
        if n == 0:
            return 0
        min_p = sys.maxsize
        max_p = -sys.maxsize
        
        for i in range(0, n):
            min_p = min(min_p, A[i])
            max_p = max(max_p, A[i]-min_p)
            
        return max_p