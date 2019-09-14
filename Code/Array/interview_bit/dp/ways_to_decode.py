class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        n = len(A)
        
        if A[0] ==  0:
            return -1
            
        if n == 1 and 0<int(A[0])<=26:
            return 1
        if n > 1:
            res =[0]*(n+1)
            res[0] = 1
            res[1] = 1
            for i in range(1, n):
                a = int(A[i])
                b = int(A[i-1:i+1])
                
                if 0<a<=9:
                    res[i+1] = res[i]
                    
                if 10<=b<=26:
                    res[i+1] = res[i+1] + res[i-1]
                    
                    
                # if res[i+1] == 0:
                #     return 0
        return res[n]
            # if res == 0:
            #     retrun -1