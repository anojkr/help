class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, S):
        
        if len(S) == 0:
            return ""
        
        word1 = min(S)
        word2 = max(S)
        
        if len(word1) == 0:
            return ""
        
        count = 0
        res = []
        for i in range(min(len(word2), len(word1))):
            if word1[0:i+1] == word2[0:i+1]:
                count += 1
                res.append(word1[i])
        
        return "".join(map(str, res))

