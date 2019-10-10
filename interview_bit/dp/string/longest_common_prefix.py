class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        
        if len(A) == 0:
            return -1
        
        w = max(A)
        z = min(A)
    
        l1 = len(w)
        l2 = len(z)

        if l2 == 0:
            return -1
        
        count = 0
        for i in range(min(l1, l2)):
            if w[0:i+1] == z[0:i+1]:
                count +=1
                
        return w[0:count]