class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n1 = len(A)+1
        n2 = len(B)+1
        
        t = [[0 for j in range(n2)]for i in range(n1)]
        
        for i in range(0, n1):
            t[i][0] = i
        for j in range(0, n2):
            t[0][j] = j
            
        for i in range(1, n1):
            for j in range(1, n2):
                if A[i-1] == B[j-1]:
                    t[i][j] = t[i-1][j-1]
                else:
                    t[i][j] = 1 + min(t[i-1][j], t[i][j-1], t[i-1][j-1])
        res = t[n1-1][n2-1]
        return res
