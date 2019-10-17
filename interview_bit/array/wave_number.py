class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        arr = A
        n = len(A)
        arr.sort()
        for i in range(0,n-1,2): 
            arr[i], arr[i+1] = arr[i+1], arr[i] 
            
        return A