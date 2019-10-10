from collections import OrderedDict
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        
        h1 = OrderedDict()
        h2 = OrderedDict()
        
        for x in A:
            if x in h1:
                h1[x]+=1
                continue
            h1[x] = 1
            
        for y in B:
            if y in h2:
                h2[y] +=1
                continue
            h2[y] = 1
            
        result = []
        for k, freq in h2.items():
            if k in h1:
                t = h1[k]
                while t>0:
                    result.append(k)
                    t = t-1
                del h1[k]
        res = sorted(h1.items())
        
        for k, item in res:
            while (item):
                result.append(k)
                item -=1
        return result
                
                
                
                
                
