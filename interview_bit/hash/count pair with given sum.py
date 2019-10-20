class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        h = { }
        for x in A:
            if x in h:
                h[x]+=1
            else:
                h[x] = 1
        count = 0
        for k, v in h.items():
            diff = B-k
            if diff in h:
                count+=1
        return count//2
    