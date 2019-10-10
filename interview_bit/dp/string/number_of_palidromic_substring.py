class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        S = list(A)
        n = len(S)
        max_len = 1
        p_begin = 0 
        count = 0
        dp = [[0 for j in range(n)]for i in range(n)]
         
        for i in range(0, n):
            dp[i][i] = 1
            count+=1
        for curr_len in range(2, n+1):
            for i in range(0, n-curr_len+1):
                j = i+curr_len-1
                if A[i] == A[j] and curr_len ==2:
                    dp[i][j] = 2
                    count+=1
                elif A[i] == A[j] and dp[i+1][j-1] > 0:
                    dp[i][j] = dp[i+1][j-1] + 2
                    count+=1
                    
        return count