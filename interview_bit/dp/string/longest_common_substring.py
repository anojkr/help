class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        
        M = len(A)
        N = len(B)
        
        dp = [[0 for j in range(N+1)] for i in range(M+1)]
        res  = 0
        for i in range(1, M+1):
            for j in range(1, N+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
                    
        # print(dp)
        return res
