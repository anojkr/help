class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, K, A):
        if not A or not A[0]: return []
        if not K: return A
        
        N = len(A)
        M = len(A[0])
        
        dp1 = A
        dp2 = [[0]*M for i in range(N)]
        
        
        
        for i in range(1,K+1):
            changed = False
            for j in range(N):
                for k in range(M):
                    V = [dp1[j][k]]
                    if j-1 >= 0: V.append(dp1[j-1][k])
                    if k-1 >= 0: V.append(dp1[j][k-1])
                    if j+1 < N: V.append(dp1[j+1][k])
                    if k+1 < M: V.append(dp1[j][k+1])
                    dp2[j][k] = max(V)
                    if dp2[j][k] != dp1[j][k]: changed = True
            if not changed: return dp1
            dp1, dp2 = dp2, dp1
        
        return dp1

