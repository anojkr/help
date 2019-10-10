class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):

        if len(A) == 1: 
            return 0
        
        cur_end, max_ladder = 0, 0
        ans = 0
        for i in range(0, len(A) - 1):
            max_ladder = max(max_ladder, i + A[i])
            if i == cur_end:
                ans += 1
                cur_end = max_ladder
        
        if cur_end >= len(A) - 1:
            return ans
        return -1
        
                
                
                
                

