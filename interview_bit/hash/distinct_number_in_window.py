from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        
        k = B
        r = []
        
        hash_h = defaultdict()
        
        i = 0
        j = 0
        n = len(A)
        
        m = 0
        
        while i < n and j < n:
            if m < k:
                if A[j] in hash_h:
                    hash_h[A[j]] += 1
                else:
                    hash_h[A[j]] = 1
                j+=1
                m+=1
                
            if m == k:
                r.append(len(hash_h.items()))
                if hash_h[A[i]] > 1:
                    hash_h[A[i]] -= 1
                else:
                    del hash_h[A[i]]
                i+=1
                m-=1
            
             
        return r
