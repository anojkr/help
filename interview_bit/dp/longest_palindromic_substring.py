class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
		
	   S = list(A)
	   n = len(S)
	   max_len = 1
	   dp = [[False for j in range(n)]for i in range(n)]
	   p_begin = 0
	    
	   for i in range(0, n):
	       dp[i][i] = True
	   
	            
	   for i in range(0, n-1):
	       if S[i] == S[i+1]:
	           dp[i][i+1] = True
	           p_begin = i
	           max_len = 2

	            
	   for curr_len in range(3, n+1):
	       flag = 0
	       for i in range(0, n-curr_len+1):
	           j = i+curr_len-1
	           if S[i] == S[j] and dp[i+1][j-1] == True:
	               dp[i][j] = True
	               if flag == 0:
	                   p_begin = i
	                   max_len = curr_len
	                   flag = 1
	               #res.append((i, max_len))
	                
	   t = S[p_begin:max_len+p_begin]
	   return "".join(map(str,t))
        # aaaabaaa
	    
