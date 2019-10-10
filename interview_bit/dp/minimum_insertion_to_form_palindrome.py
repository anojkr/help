
def Min(a, b): 
	return min(a, b) 

def findMinInsertionsDP(str1, n): 

	table = [[0 for i in range(n)] 
				for i in range(n)] 
	l, h, gap = 0, 0, 0

	# Fill the table 
	for gap in range(1, n): 
		for i in range(0, n-gap):
		    j = i + gap
		    if str1[i] == str1[j]:
		        table[i][j] = table[i + 1][j - 1]
		    else:
		        table[i][j] = (Min(table[i][j - 1],table[i + 1][j]) + 1)
	print(table)
	return table[0][n - 1]
    
# Driver Code
str1 = "geesks"
print(findMinInsertionsDP(str1, len(str1))) 
