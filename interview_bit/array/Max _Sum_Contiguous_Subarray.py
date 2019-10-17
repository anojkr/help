import sys
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        c = 0
        g = A[0]
        n = len(A)
        
        for i in range(0, n):
            c = c+A[i]
            g = max(g , c)
            
            if c < 0:
                c = 0
        return g
