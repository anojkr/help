
# https://www.geeksforgeeks.org/majority-element/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        
        N = len(A)
        candidate = A[0]
        count = 0
        
        for i in range(0, N):
            if count == 0:
                candidate = A[i]
                count = 1
            else:
                if candidate == A[i]:
                    count +=1
                else:
                    count -=1
                    
        m = 0
        for i in range(0, N):
            if candidate == A[i]:
                m += 1
                
        if m > N//2:
            return candidate
        else:
            return 0


            