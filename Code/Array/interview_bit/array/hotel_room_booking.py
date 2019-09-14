# from itertools import zip
class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        n = len(arrive)
        arr=arrive
        dep=depart

        arr.sort() 
        dep.sort() 
       
        plat_needed = 1
        result = 1
        i = 1
        j = 0

        while (i < n and j < n): 
            if (arr[i] < dep[j]): 
                plat_needed+=1
                i+=1

                if (plat_needed > result):  
                    result = plat_needed 

            else: 
                plat_needed-=1
                j+=1
        
        if result > K:
            return 0
        return 1
