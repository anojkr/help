class Solution(object):
    
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return 0
        aux = [0]*(len(s) + 1)
        aux[0] = 1
        for i in xrange(len(s)):
            for j in xrange(i, -1, -1):
                if aux[j] and s[j : i + 1] in wordDict:
                    aux[i + 1] = 1
                    break

        return aux[len(s)]

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        words = set(B)
        i = 0
        n = len(A)
        dp = [0 for i in range(n)]
        while i < n:
            j = i
            while j >= 0:
                if A[j:i+1] in words:
                    dp[i] = 1 if j == 0 else dp[j-1]
                if dp[i]:
                    break
                j -= 1
            i += 1
        
        return dp[n-1]
                                 


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        s = A
        d = set(B)
        segmented = [1];
        for i in range (0, len(s)):
            segmented.append(0)
            for j in range(i,-1,-1):
                if segmented[j] and s[j:i+1] in d:
                    segmented[i+1] = 1
                    break
        return segmented[len(s)]