Find a pair of elements swapping which makes sum of two arrays same

def solve(A, B):
	goal = (sum(A) - sum(B))/2
	A.sort()
	B.sort()

	target = goal/2

	if target == 0:
		return -1
		
	i = 0, j = 0

	while i < len(A) and j < len(B):
		diff = A[i] - B[i]

		if diff == target:
			print(A[i], B[i])
			break
			
		elif diff < target:
			i+=1

		elif diff > target:
			j+=1

