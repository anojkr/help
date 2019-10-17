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