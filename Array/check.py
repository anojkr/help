# Python3 program to rotate an array by 
# d elements 
# Function to left rotate arr[] of size n by d 
def leftRotate(arr, d, n): 
	g_c_d = gcd(d, n)
	print(g_c_d)
	for i in range(g_c_d): 
		
		# move i-th values of blocks 
		temp = arr[i] 
		j = i 
		while 1: 
			k = j + d 
			if k >= n: 
				k = k - n 
			if k == i: 
				break
			arr[j] = arr[k] 
			j = k 
		arr[j] = temp 

# UTILITY FUNCTIONS 
# function to print an array 
def printArray(arr, size): 
	for i in range(size): 
		print ("% d" % arr[i], end =" ") 

# Fuction to get gcd of a and b 
def gcd(a, b): 
	if b == 0: 
		return a; 
	else: 
		return gcd(b, a % b) 

# Driver program to test above functions 
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 5, 7) 
printArray(arr, 7) 

# This code is contributed by Shreyanshi Arun 
