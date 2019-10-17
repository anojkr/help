
def solve(n):


	count = 0

	while 1 :
		if n == 0:
			break

		if n%2 == 1:
			n = n-1

		elif n != 0 and n%2 == 0:
			n = n/2

		count += 1
		print("n val = ",n)

	return count

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
    	n = int(input())
    	t = t -1
    	print(solve(n))
    
