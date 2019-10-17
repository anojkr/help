
def solve(n):

	if n == 0:
		return 0:

	a = [0]*n
	b = [0]*n

	a[0] = b[0] = 1

	for k in range(1, n):
		a[i] = a[i-1] + b[i-1]
		b[i] = a[i-1]

	return a[n-1]+b[n-1]