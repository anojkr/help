class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        S = list(s)
        n = len(S)
        max_len = 1
        p_begin = 0 
        dp = [[0 for j in range(n)]for i in range(n)]
         
        for i in range(0, n):
            dp[i][i] = 1
            
        for curr_len in range(2, n+1):
            flag = 1
            
            for i in range(0, n-curr_len+1):
                j = i+curr_len-1

                if S[i] == S[j] and curr_len ==2:
                    dp[i][j] = 2
                    p_begin = i
                    max_len = 2
                    
                elif S[i] == S[j] and dp[i+1][j-1] > 0:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if flag == 1: 
                        p_begin = i
                        max_len = curr_len
                        flag = 0
        t  = S[p_begin : p_begin+max_len]
        return "".join(map(str, t))
            
            

        
        