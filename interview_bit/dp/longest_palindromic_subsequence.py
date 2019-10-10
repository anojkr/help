class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        n = len(A)
        
        dp = [[0 for j in range(n)]for i in range(n)]
        
        for i in range(0, n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if A[i] == A[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][n-1]
                