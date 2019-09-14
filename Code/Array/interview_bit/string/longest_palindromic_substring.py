class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)
        if n <= 1:
            return A
        cs = 2*n - 1

        ans = ''
        for c in range(cs):
            i = int(c/2)
            j=i
            if c%2 != 0:
                i = i+1
            while i < n and j >= 0 and A[i] == A[j]:
                if len(ans) < i-j+1:
                    ans = A[j:i+1]
                i+=1
                j-=1

        
        return ans

