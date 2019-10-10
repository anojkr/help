# cook your dish here

def Min(a, b): 
	return min(a, b) 

def findMinInsertionsDP(str1, n): 

	table = [[0 for i in range(n)] 
				for i in range(n)] 
	l, h, gap = 0, 0, 0

	# Fill the table 
	for curr_len in range(2, n+1): 
		for i in range(0, n-curr_len+1):
		    j = i + curr_len-1
		    
		    if str1[i] == str1[j]:
		        table[i][j] = table[i + 1][j - 1]
		    else:
		        table[i][j] = (Min(table[i][j - 1],table[i + 1][j]) + 1)
	print(table)
	return table[0][n - 1]
    
# Driver Code
str1 = "geesks"
print(findMinInsertionsDP(str1, len(str1))) 
