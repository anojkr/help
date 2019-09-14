class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        
        n = len(A)
        m = len(A[0])
        # print(n,m)
        
        t = [[0 for j in range(m)] for i in range(n)]
        
        t[0][0] = A[0][0]
        
        for i in range(1, n):
            t[i][0] = t[i-1][0] + A[i][0]
            
        for j in range(1, m):
            t[0][j] = t[0][j-1] + A[0][j]
            
        for i in range(1, n):
            for j in range(1, m):
                t[i][j] = min(t[i-1][j], t[i][j-1] ) + A[i][j]
        # print(t)
        return t[n-1][m-1]    
