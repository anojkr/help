class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        
        n = len(A)
        
        if int(A[0]) == 0:
            return 0
            
        if n == 0:
            return 0
                       
        res = [0 for i in range(n+1)]
        
        res[0] = 1
        res[1] = 1
        
        for i in range(1, n):
            v1 = int(A[i])
            v2 = int(A[i-1:i+1])
            
            if 0 < v1<=9:
                res[i+1] = res[i]
                                
            if 10 <= v2 <= 26:
                res[i+1] = res[i+1] + res[i-1]

        return res[n]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            