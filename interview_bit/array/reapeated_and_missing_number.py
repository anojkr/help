def solve_better_method(A):
    n = len(A)
    for i in range(0, n):
        d = abs[A[i]]-1

        if A[d] > 0:
            A[d] = -A[d]
        else:
            print("repeating number", i+1)
    for i in range(0, k):
        if A[k] > 0:
            print("missing elemnt", i+10)
            break


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