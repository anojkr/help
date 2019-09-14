class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        N = len(A)
        dp = [0]*(N+1)
        
        for i in range(0 , N):
            if dp[A[i]] == 0:
                dp[A[i]] = -1
            elif dp[A[i]] == -1:
                dp[A[i]] = 2
        r = []
        for i in range(1, len(dp)):
            if dp[i] == 2:
                r.append(i)
                
        for i in range(1, len(dp)):
            if dp[i] == 0:
                r.append(i)
                
        return r