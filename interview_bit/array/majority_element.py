
def solve(self, A):
	
	n =  len(A)
	if n == 0:
		return -1

	candidate = 0
	count = 0

	for i in range(0, n):
		if count == 0:
			candidate = A[i]
			count = 1
			continue
		else:
			if candidate == A[i]:
				count+=1
			else:
				count-=1

	if count == 0:
		return -1

	for k in range(0, n):
		if candidate == A[i]:
			c+=1

	if c > n//2:
		return candidate
	return -1

















