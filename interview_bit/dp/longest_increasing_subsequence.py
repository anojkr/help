class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        
        n = len(A)
        dp = [1 for i in range(n)]
        
        for i in range(0, n):
            for j in range(0, i):
                if A[i] > A[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        return max(dp)