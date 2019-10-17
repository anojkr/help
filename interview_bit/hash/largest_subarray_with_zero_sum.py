class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        
        curr = 0
        d = {0: 0}
        res = 0
        e = -1
        s = -1
        
        for i in range(len(A)):
            curr = curr + A[i]
            if curr not in d:
                d[curr]  = i
                
            elif curr == 0:
                if res < i+1:
                    res = i+1
                    s = 0
                    e = i+1
                    
            elif curr in d:
                t = i - d[curr]
                if res < t:
                    res = t
                    s = d[curr]+1
                    e = i+1

        return A[s:e]

