
def permute(A, l, h):

	if l == h :
		print(A)
	
	else:

		for i in range(l, r+1):
			swap(A[i], A[l])
			permute(A, l+1, h)
			swap(A[i], A[l])